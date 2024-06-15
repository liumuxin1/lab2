import datetime
import math
from django.shortcuts import render, redirect
from django.db import Error as djangoDBError
from django.http import HttpResponse
from django.contrib import messages
from BankManage.models import *
from django.db import transaction
from django.db import connection
import json

# Create your views here.
FILEROOT = 'BankManage/'
EPS = 1e-4


def index(request):
    #开始页面，包含四个功能的Entry
    return render(request, FILEROOT+'index.html', {})


def client(request):
    #客户管理
    if request.session.get('client_view_change') == None:
        request.session['client_view_change'] = 'add'
    if request.method == 'POST':
        func = request.POST.get('function')
        if func == 'add':
            request.session['client_view_change'] = 'add'
            #对应添加客户的功能
            attrs = request.POST.dict()
            if len(Client.objects.filter(ID_card=attrs['ID_card'])) == 0:
                #不存在该客户，可以添加
                obj = Client(ID_card=attrs['ID_card'],
                             name=attrs['name'],
                             phone=attrs['phone'],
                             address=attrs['address'],
                             img=request.FILES.get('img')
                             )
                try:
                    obj.save()
                except djangoDBError as e:
                    messages.error(request, 'ERROR: '+str(e))
                except:
                    messages.error(request, 'ERROR: Failed to save client!')
                    raise
                else:
                    messages.info(request, 'SUCCESS: New client saved!')
            else:
                messages.error(request, 'ERROR: Client already exists!')
        elif func == 'modify img':
            request.session['client_view_change'] = 'img'
            attrs = request.POST.dict()
            objs = Client.objects.filter(ID_card=attrs['ID_card'])
            if (len(objs) != 1):
                messages.error(request, 'ERROR: client not found!')
            else:
                obj = objs[0]
                obj.img=request.FILES.get('img')
                try:
                    obj.save()
                except djangoDBError as e:
                    messages.error(request, 'ERROR: '+str(e))
                except:
                    messages.error(request, 'ERROR: Failed to modify image!')
                    raise
                else:
                    messages.info(request, 'SUCCESS: image modified!')

        elif func == 'query':
            request.session['client_view_change'] = 'qmd'
            #查询
            attrs = request.POST.dict()
            attrs.pop('function')
            filters = {}
            for key, value in attrs.items():
                if value != '':
                    filters[key] = value
            try:
                objs = Client.objects.filter(**filters)
            except:
                messages.error(request, 'ERROR: Invalid input!')
            else:
                #将用户的信息显示出来
                res = []
                for obj in objs:
                    if obj.img.name:
                        res.append({'ID_card': obj.ID_card,
                                    'name': obj.name,
                                    'phone': obj.phone,
                                    'address': obj.address,
                                    'img': obj.img
                                    })
                    else:
                        res.append({'ID_card': obj.ID_card,
                                    'name': obj.name,
                                    'phone': obj.phone,
                                    'address': obj.address,
                                    })
                return render(request, FILEROOT+'client.html', {'view_change': request.session['client_view_change'], 'result': res})
        elif func == 'delete':
            request.session['client_view_change'] = 'qmd'
            success_flag = True
            for ID_card in request.POST.get('selectedIDs').split(','):
                try:
                    obj = Client.objects.get(pk=ID_card)
                except:
                    success_flag = False
                    messages.error(
                        request, 'ERROR: Client not found:%s!' % ID_card)
                else:
                    try:
                        obj.delete()
                    except djangoDBError as e:
                        success_flag = False
                        messages.error(request, 'ERROR: '+str(e))
                    except:
                        success_flag = False
                        messages.error(
                            request, 'ERROR: Cannot delete client:%s!' % ID_card)
                        raise
            if success_flag:
                messages.info(request, 'SUCCESS: Client deleted!')
        elif func == 'modify':
            request.session['client_view_change'] = 'qmd'
            modified_data = json.loads(request.POST.get('modifiedData'))
            success_flag = True
            for clt in modified_data:
                try:
                    obj = Client.objects.get(pk=clt['ID_card'])
                except:
                    success_flag = False
                    messages.error(
                        request, 'ERROR: Client not found:%s!' % clt['ID_card'])
                else:
                    try:
                        obj.name = clt['name']
                        obj.phone = clt['phone']
                        obj.address = clt['address']
                        obj.save()
                    except djangoDBError as e:
                        success_flag = False
                        messages.error(request, 'ERROR: '+str(e))
                    except:
                        success_flag = False
                        messages.error(
                            request, 'ERROR: Cannot modify client:%s!' % clt['ID_card'])
                        raise
            if success_flag:
                messages.info(request, 'SUCCESS: Client modified!')
        return redirect('client')
    else:
        return render(request, FILEROOT+'client.html', {'view_change': request.session['client_view_change'], })


def account(request):
    #账户管理
    if request.session.get('account_view') == None:
        request.session['account_view'] = 'add'
    if request.method == 'POST':
        func = request.POST.get('function')
        if func == 'add':
            request.session['account_view'] = 'add'
            attrs = request.POST.dict()
            account_type = attrs['accountType']
            print(attrs)
            if account_type == 'storeaccount':
                if len(StoreAccount.objects.filter(Account_ID=attrs['Account_ID'], fk_bank=attrs['fk_bank'])) == 0:
                    #不存在该账户，可以添加
                    try:
                        #这里涉及两个表，前者正常后者出错会违反原子性，需要特别处理
                        account_obj = StoreAccount(Account_ID=attrs['Account_ID'],
                                                   fk_bank=Bank.objects.get(
                                                       pk=attrs['fk_bank']),
                                                   balance=attrs['balance'],
                                                   open_date=attrs['open_date'],
                                                   rate=attrs['rate'],
                                                   currency_type=attrs['currency_type'])
                        #新建账户到用户的联系
                        relation_obj = OpenStore(fk_client=Client.objects.get(
                                                     pk=attrs['fk_client']),
                                                 fk_account=account_obj)
                        with transaction.atomic():
                            account_obj.save()
                            relation_obj.save()
                    except djangoDBError as e:
                        messages.error(request, 'ERROR: '+str(e))
                    except:
                        messages.error(
                            request, 'ERROR: Cannot create store account!')
                        raise
                    else:
                        messages.info(
                            request, 'SUCCESS: Store account created!')
                else:
                    messages.error(request, 'ERROR: Account already exists!')
            if account_type == 'checkaccount':
                if len(CheckAccount.objects.filter(Account_ID=attrs['Account_ID'], fk_bank=attrs['fk_bank'])) == 0:
                    #不存在该账户，可以添加
                    try:
                        account_obj = CheckAccount(Account_ID=attrs['Account_ID'],
                                                   fk_bank=Bank.objects.get(
                                                       pk=attrs['fk_bank']),
                                                   balance=attrs['balance'],
                                                   open_date=attrs['open_date'],
                                                   overdraft=attrs['overdraft'])
                        #新建账户到用户的联系
                        relation_obj = OpenCheck(fk_client=Client.objects.get(
                                                     pk=attrs['fk_client']),
                                                 fk_account=account_obj)
                        #这里涉及两个表，前者正常后者出错会违反原子性，需要特别处理
                        with transaction.atomic():
                            account_obj.save()
                            relation_obj.save()
                    except djangoDBError as e:
                        messages.error(request, 'ERROR: '+str(e))
                    except:
                        messages.error(
                            request, 'ERROR: Cannot create check account!')
                        raise
                    else:
                        messages.info(
                            request, 'SUCCESS: check account created!')
                else:
                    messages.error(request, 'ERROR: Account already exists!')
        elif func == 'query':
            request.session['account_view'] = 'query'
            attrs = request.POST.dict()
            #剔除attrs中无用项
            attrs.pop('function')
            account_type = attrs['accountType']
            attrs.pop('accountType')
            if account_type == 'storeaccount':
                attrs.pop('overdraft')
            if account_type == 'checkaccount':
                attrs.pop('rate')
                attrs.pop('currency_type')
            #改键名
            attrs['fk_bank_id'] = attrs.pop('fk_bank')
            print(attrs)
            #添加非空约束
            if account_type == 'storeaccount':
                sql = 'SELECT * FROM BankManage_{0}, BankManage_openstore WHERE BankManage_{0}.Account_ID = fk_account_id'.format(account_type)
            if account_type == 'checkaccount':
                sql = 'SELECT * FROM BankManage_{0}, BankManage_opencheck WHERE BankManage_{0}.Account_ID = fk_account_id'.format(account_type)
            for key, val in attrs.items():
                if val != '':
                    sql += " AND {0}='{1}'".format(key, val)
            print(sql)
            res = []
            success_flag = False
            try:
                if account_type == 'storeaccount':
                    qry = StoreAccount.objects.raw(sql)
                if account_type == 'checkaccount':
                    qry = CheckAccount.objects.raw(sql)
                objs = [obj for obj in qry]
            except:
                messages(request, "ERROR: Failed to execute sql query!")
                raise
            else:
                success_flag = True
                if account_type == 'storeaccount':
                    for obj in objs:
                        res.append({
                            'Account_ID': obj.Account_ID,
                            'fk_client_id': obj.fk_client_id,
                            'fk_bank': obj.fk_bank.title,
                            'balance': obj.balance,
                            'open_date': str(obj.open_date),
                            'rate': obj.rate,
                            'currency_type': obj.currency_type,
                        })
                if account_type == 'checkaccount':
                    for obj in objs:
                        res.append({
                            'Account_ID': obj.Account_ID,
                            'fk_client_id': obj.fk_client_id,
                            'fk_bank': obj.fk_bank.title,
                            'balance': obj.balance,
                            'open_date': str(obj.open_date),
                            'overdraft': obj.overdraft,
                        })
            if success_flag:
                messages.info(request, 'SUCCESS: Query completed!')
                request.session['account_view'] = 'modify'
                qry = Bank.objects.raw(
                    'SELECT DISTINCT title FROM BankManage_bank;')
                banks = [obj.title for obj in qry]
                return render(request, FILEROOT+'account.html',
                              {'view': request.session['account_view'],
                               'banks': banks,
                               'result': res,
                               'account_type': account_type
                               })
        elif func == 'delete':
            print(request.POST.dict())
            request.session['account_view'] = 'modify'
            account_type = request.POST.get('accountType')
            success_flag = True
            for info in json.loads(request.POST.get('deleteData')):
                try:
                    if account_type == 'storeaccount':
                        account_obj = StoreAccount.objects.filter(
                            Account_ID=info['Account_ID'])[0]
                        open_obj = OpenStore.objects.filter(
                            fk_account=StoreAccount.objects.get(Account_ID=info['Account_ID']))[0]
                    if account_type == 'checkaccount':
                        account_obj = CheckAccount.objects.filter(
                            Account_ID=info['Account_ID'])[0]
                        open_obj = OpenCheck.objects.filter(
                            fk_account=CheckAccount.objects.get(Account_ID=info['Account_ID']))[0]
                except:
                    success_flag = False
                    messages.error(
                        request, 'ERROR: Account not found!')
                    raise
                else:
                    try:
                        account_obj.delete()
                        open_obj.delete()
                    except djangoDBError as e:
                        success_flag = False
                        messages.error(request, 'ERROR: '+str(e))
                    except:
                        success_flag = False
                        messages.error(
                            request, 'ERROR: Cannot delete account!')
                        raise
            if success_flag:
                messages.info(request, 'SUCCESS: Account deleted!')
                request.session['account_view'] = 'query'
        elif func == 'modify':
            print(request.POST.dict())
            request.session['account_view'] = 'modify'
            account_type = request.POST.get('accountType')
            success_flag = True
            for info in json.loads(request.POST.get('modifiedData')):
                try:
                    if account_type == 'storeaccount':
                        obj = StoreAccount.objects.filter(
                            Account_ID=info['Account_ID'], fk_bank=Bank.objects.get(pk=info['fk_bank']))[0]
                    if account_type == 'checkaccount':
                        obj = CheckAccount.objects.filter(
                            Account_ID=info['Account_ID'], fk_bank=Bank.objects.get(pk=info['fk_bank']))[0]
                except:
                    success_flag = False
                    messages.error(
                        request, 'ERROR: Account not found!')
                    raise
                else:
                    try:
                        if account_type == 'storeaccount':
                            obj.balance = info['balance']
                            obj.open_date = info['open_date']
                            obj.rate = info['rate']
                            obj.currency_type = info['currency_type']
                        if account_type == 'checkaccount':
                            obj.balance = info['balance']
                            obj.open_date = info['open_date']
                            obj.overdraft = info['overdraft']
                        obj.save()
                    except djangoDBError as e:
                        success_flag = False
                        messages.error(request, 'ERROR: '+str(e))
                    except:
                        success_flag = False
                        messages.error(
                            request, 'ERROR: Cannot modify account!')
                        raise
            if success_flag:
                messages.info(request, 'SUCCESS: Account modified!')
                request.session['account_view'] = 'query'
        elif func == 'transfer':        
            attrs = request.POST.dict()
            with connection.cursor() as cursor:
                sql = "call bank_transfer ({0}, {1}, {2}, @state)".format(str(attrs['Account_ID_from']), str(attrs['Account_ID_to']), attrs['money'])
                cursor.execute(sql)
                sql = 'select @state'
                cursor.execute(sql)
                row = cursor.fetchone()[0]
                if (row == 0):
                    messages.info(request, 'SUCCESS!')
                    request.session['account_view'] = 'query'
                elif (row == 1):
                    messages.error(request, 'ERROR: sqlexception!')
                elif (row == 2):
                    messages.error(request, 'ERROR: no storeaccount!')
                elif (row == 3):
                    messages.error(request, 'ERROR: balance is not enough!')
                elif (row == 4):
                    messages.error(request, 'ERROR: currency type not match!')
                else:
                    messages.error(request, 'ERROR: !')

        return redirect('account')
    else:
        qry = Bank.objects.raw('SELECT DISTINCT title FROM BankManage_bank;')
        banks = [obj.title for obj in qry]
        return render(request, FILEROOT+'account.html',
                      {'view': request.session['account_view'],
                       'banks': banks,
                       })


def loan_manage(request):
    if request.session.get('loan_view') == None:
        request.session['loan_view'] = False
    if request.method == 'POST':
        print(request.POST.dict())
        func = request.POST.get('function')
        if func == 'add':
            request.session['loan_view'] = 'add'
            attrs = request.POST.dict()
            if len(Loan.objects.filter(Loan_ID=attrs['Loan_ID'])) == 0:
                try:
                    clients = [attrs['fk_client']]
                    clt_loan_objs = []
                    loan_obj = Loan(Loan_ID=attrs['Loan_ID'],
                                    money=attrs['money'])
                    for clt in clients:
                        clt_loan_objs.append(ClientLoan(fk_loan=loan_obj,
                                                        fk_client=Client.objects.get(pk=clt)))
                    with transaction.atomic():
                        loan_obj.save()
                        for loan_obj in clt_loan_objs:
                            loan_obj.save()
                except djangoDBError as e:
                    messages.error(request, 'ERROR: '+str(e))
                except:
                    messages.error(
                        request, 'ERROR: Cannot create loan!')
                    raise
                else:
                    messages.info(request, 'SUCESS: Loan created!')
            else:
                messages.error(request, 'ERROR: Loan already exists!')
        elif func == 'query':
            request.session['loan_view'] = 'query'
            attrs = request.POST.dict()
            filters = {}
            if attrs['Loan_ID'] != '':
                filters['Loan_ID'] = attrs['Loan_ID']
            loan_objs = Loan.objects.filter(**filters)
            res = []
            for loan_obj in loan_objs:
                clients = ClientLoan.objects.filter(fk_loan=loan_obj)
                with connection.cursor() as cursor:
                    print(loan_obj.Loan_ID)
                    sql = "select pay({0});".format(loan_obj.Loan_ID)
                    cursor.execute(sql)
                    paid = cursor.fetchone()
                    print(paid)
                for client in clients:
                    id = client.fk_client
                    res.append({'status': loan_obj.status,
                            'Loan_ID': loan_obj.Loan_ID,
                            'client_id': id.ID_card,
                            'money': '%.3f' % loan_obj.money,
                            'paid_money': '%.3f' % paid})
            qry = Bank.objects.raw(
                'SELECT DISTINCT title FROM BankManage_bank;')
            banks = [obj.title for obj in qry]
            return render(request, FILEROOT+'loan_manage.html',
                          {'view_change': request.session['loan_view'],
                           'banks': banks,
                           'result': res})
        elif func == 'delete':
            request.session['loan_view'] = True
            success_flag = True
            for Loan_ID in json.loads(request.POST.get('deleteIDs')):
                try:
                    loan_obj = Loan.objects.get(pk=Loan_ID)
                except:
                    success_flag = False
                    messages.error(
                        request, 'ERROR: Loan not found:%s!' % Loan_ID)
                    raise
                else:
                    try:
                        loan_obj.delete()
                    except djangoDBError as e:
                        success_flag = False
                        messages.error(request, 'ERROR: '+str(e))
                    except:
                        success_flag = False
                        messages.error(request, 'ERROR: Cannot delete loan!')
                        raise
            if success_flag:
                messages.info(request, 'SUCCESS: Loan deleted!')
            
        return redirect('loan_manage',)
    else:
        qry = Bank.objects.raw('SELECT DISTINCT title FROM BankManage_bank;')
        banks = [obj.title for obj in qry]
        return render(request, FILEROOT+'loan_manage.html',
                      {'view_change': request.session['loan_view'],
                       'banks': banks, })


def loan_issue(request):
    if request.method == 'POST':
        attrs = request.POST.dict()
        print(attrs)
        #添加记录到Payment表
        try:
            obj = Payment(fk_loan=Loan.objects.get(Loan_ID=attrs['fk_loan']),
                          pay_date=attrs['pay_date'],
                          pay_money=attrs['pay_money'])
            obj.save()
        except djangoDBError as e:
            messages.error(request, 'ERROR: '+str(e))
        except:
            messages.error(request, 'ERROR: Cannot create payment!')
        else:
            messages.info(request, 'SUCCESS: Payment created!')
        return redirect('loan_issue')
    else:
        return render(request, FILEROOT+'loan_issue.html')


def statistics(request):
    qry = Bank.objects.raw('SELECT DISTINCT title FROM BankManage_bank;')
    banks = [obj.title for obj in qry]
    #储蓄业务的统计
    storing = []
    store_qry = StoreAccount.objects.raw(
        'SELECT * FROM BankManage_storeaccount WHERE fk_bank_id is not NULL;')
    check_qry = CheckAccount.objects.raw(
        'SELECT * FROM BankManage_checkaccount WHERE fk_bank_id is not NULL;')
    objs = [obj for obj in store_qry]
    for obj in objs:
        storing.append({'bank': obj.fk_bank.title,
                        'money': obj.balance,
                        'date': obj.open_date,
                        'currency_type': obj.currency_type})
    objs = [obj for obj in check_qry]
    for obj in objs:
        storing.append({'bank': obj.fk_bank.title,
                        'money': obj.balance,
                        'date': obj.open_date,
                        'currency_type': 'CNY'})
    #贷款业务
    loans = {b: 0 for b in banks}
    loan_qry = Loan.objects.raw(
        'SELECT * FROM BankManage_loan WHERE fk_bank_id is not NULL;')
    for obj in loan_qry:
        bank_ID = obj.fk_bank.title
        loans[bank_ID] += obj.money
    #用户数
    clt_by_bank = {b: set([]) for b in banks}
    clt_store_qry = OpenStore.objects.raw(
        'SELECT * FROM BankManage_openstore, BankManage_storeaccount WHERE BankManage_openstore.fk_account_id = BankManage_storeaccount.Account_ID and fk_account_id is not NULL and fk_client_id is not NULL;')
    clt_check_qry = OpenCheck.objects.raw(
        'SELECT * FROM BankManage_opencheck, BankManage_checkaccount WHERE BankManage_opencheck.fk_account_id = BankManage_checkaccount.Account_ID and fk_account_id is not NULL and fk_client_id is not NULL;')
    clt_store_obj = [obj for obj in clt_store_qry] + \
        [obj for obj in clt_check_qry]
    for obj in clt_store_obj:
        clt_by_bank[obj.fk_bank_id].add(obj.fk_client.ID_card)
    clt_loan_qry = ClientLoan.objects.raw(
        'SELECT * from BankManage_clientloan,BankManage_loan where BankManage_clientloan.fk_loan_id=BankManage_loan.loan_ID AND BankManage_loan.fk_bank_id is not NULL AND BankManage_clientloan.fk_loan_id is not NULL AND BankManage_clientloan.fk_client_id is not NULL;')
    for obj in clt_loan_qry:
        clt_by_bank[obj.fk_loan.fk_bank.title].add(obj.fk_client.ID_card)
    num_by_bank = {key: len(val) for key, val in clt_by_bank.items()}
    min_year = math.inf
    max_year = -math.inf
    store_CNY = {}
    store_USD = {}
    recent = datetime.date(1,1,1)
    for store in storing: #计算年份范围
        if store['date']>recent:
            recent = store['date']
        year = store['date'].year
        if year < min_year:
            min_year = year
        if year > max_year:
            max_year = year
    for year in range(min_year, max_year+1):
        store_CNY[year] = {b: 0 for b in banks}
        store_USD[year] = {b: 0 for b in banks}
    
    for store in storing:
        if(store['currency_type'] == 'CNY'):
            sdate = store['date']
            store_CNY[sdate.year][store['bank']] += store['money']
        elif(store['currency_type'] == 'USD'):
            sdate = store['date']
            store_USD[sdate.year][store['bank']] += store['money']

    print(store_USD)
    print(store_CNY)    
    for date, bankinfo in store_CNY.items():
        for bank, money in bankinfo.items():
            store_CNY[date][bank] = '%.3f' % money
    
    for date, bankinfo in store_USD.items():
        for bank, money in bankinfo.items():
            store_USD[date][bank] = '%.3f' % money
    
    return render(request, FILEROOT+'statistics.html',
                  {'banks': banks,
                   'loans': loans,
                   'clients': num_by_bank,
                   'storeCNY': store_CNY,
                   'storeUSD': store_USD,
                   })
