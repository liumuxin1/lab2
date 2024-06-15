from django.db import models

# Create your models here.

class Bank(models.Model):
    title = models.CharField(max_length=100,primary_key=True)
    city = models.CharField(max_length=50)
    assset = models.FloatField(default=0)

class Client(models.Model):
    ID_card = models.CharField(max_length=18,primary_key=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=11)
    address = models.CharField(max_length=200)
    img = models.ImageField(upload_to='img', null=True, blank=True)

class Department(models.Model):
    id = models.AutoField(primary_key=True)

    Depart_ID = models.CharField(max_length=20)
    fk_bank = models.ForeignKey(Bank,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    dtype = models.CharField(max_length=20)

    class Meta:
        unique_together=("Depart_ID","fk_bank")

class Employee(models.Model):
    ID_card = models.CharField(max_length=18,primary_key=True)
    fk_bank = models.ForeignKey(Bank,on_delete=models.SET_NULL,null=True)
    fk_department = models.ForeignKey(Department,on_delete=models.SET_NULL,null=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=11)
    address = models.CharField(max_length=200)
    entry_date = models.DateField()

class Service(models.Model):
    id = models.AutoField(primary_key=True)
    
    client = models.ForeignKey(Client,on_delete=models.SET_NULL,null=True)
    employee = models.ForeignKey(Employee,on_delete=models.SET_NULL,null=True)
    stype = models.CharField(max_length=20)

    class Meta:
        unique_together=("client","employee")


class StoreAccount(models.Model):
    Account_ID = models.CharField(max_length=50,primary_key=True)
    fk_bank = models.ForeignKey(Bank,on_delete=models.SET_NULL,null=True)
    balance = models.FloatField(default=0)
    open_date = models.DateField()
    rate = models.FloatField()
    currency_type = models.CharField(max_length=20)
    class Meta:
        unique_together=("Account_ID","fk_bank")

class CheckAccount(models.Model):
    Account_ID = models.CharField(max_length=50,primary_key=True)
    fk_bank = models.ForeignKey(Bank,on_delete=models.SET_NULL,null=True)
    balance = models.FloatField(default=0)
    open_date = models.DateField()
    overdraft =  models.FloatField(default=0)
    class Meta:
        unique_together=("Account_ID","fk_bank")

class OpenStore(models.Model):
    id = models.AutoField(primary_key=True)
    
    fk_client = models.ForeignKey(Client,on_delete=models.PROTECT,null=True)
    fk_account = models.ForeignKey(StoreAccount,on_delete=models.CASCADE,null=True)
    last_access = models.DateField(auto_now=True)

class OpenCheck(models.Model):
    id = models.AutoField(primary_key=True)
    
    fk_client = models.ForeignKey(Client,on_delete=models.PROTECT,null=True)
    fk_account = models.ForeignKey(CheckAccount,models.CASCADE,null=True)
    last_access = models.DateField(auto_now=True)

class Loan(models.Model):
    Loan_ID = models.CharField(max_length=50,primary_key=True)
    fk_bank = models.ForeignKey(Bank,on_delete=models.SET_NULL,null=True)
    money = models.FloatField(default=0)
    status = models.CharField(max_length=20, default='未支付')

class Payment(models.Model):
    Payment_ID = models.AutoField(primary_key=True)
    fk_loan = models.ForeignKey(Loan,on_delete=models.SET_NULL,null=True)
    pay_date = models.DateField()
    pay_money = models.FloatField()

class ClientLoan(models.Model):
    id = models.AutoField(primary_key=True)
    
    fk_loan = models.ForeignKey(Loan,on_delete=models.SET_NULL,null=True)
    fk_client = models.ForeignKey(Client,on_delete=models.PROTECT,null=True)

    class Meta:
        unique_together=("fk_loan","fk_client")
