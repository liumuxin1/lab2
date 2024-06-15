drop procedure if exists bank_transfer;
delimiter //
create procedure bank_transfer (in ac_from varchar(50), in ac_to varchar(50), in money double, out state int)
begin
    declare s int default 0;
    declare countf int;
    declare countt int;
    declare bal double;
    declare type1 varchar(20);
    declare type2 varchar(20);
    declare continue handler for sqlexception set s = 1;
    start transaction;

    select count(*) from BankManage_storeaccount where Account_ID = LPAD(ac_from, 10, '0') into countf;
    select count(*) from BankManage_storeaccount where Account_ID = LPAD(ac_to, 10, '0') into countt;
    if countf = 0 or countt = 0 then
        set s = 2;
    end if;
    select balance from BankManage_storeaccount where Account_ID = LPAD(ac_from, 10, '0') into bal;
    if bal < money then
        set s = 3;
    end if;
    select currency_type from BankManage_storeaccount where Account_ID = LPAD(ac_from, 10, '0') into type1;
    select currency_type from BankManage_storeaccount where Account_ID = LPAD(ac_to, 10, '0') into type2;
    if type1 != type2 then
        set s = 4;
    end if;

    update BankManage_storeaccount set balance = balance - money where Account_ID = LPAD(ac_from, 10, '0');
    update BankManage_storeaccount set balance = balance + money where Account_ID = LPAD(ac_to, 10, '0');

    if s = 0 then
        commit;
    else
        rollback;
    end if;

    set state = s;
end //
delimiter ;

drop trigger if exists loan_status;
delimiter //
create trigger loan_status after insert on BankManage_payment for each row
begin
    declare m double;
    declare p double;
    select money from BankManage_loan where Loan_ID = new.fk_loan_id into m;
    select sum(pay_money) from BankManage_payment where fk_loan_id = new.fk_loan_id into p;
    if p > 0 and p < m then
        update BankManage_loan set status = '支付中' where Loan_ID = new.fk_loan_id;
    elseif p >= m then
        update BankManage_loan set status = '已全部支付' where Loan_ID = new.fk_loan_id;
    end if;
end //
delimiter ;

drop function if exists pay;
delimiter //
create function pay (loan_id varchar(50))
returns double
reads sql data
begin
    declare flag int;
    declare money double;
    select count(*) from BankManage_payment where fk_loan_id = LPAD(loan_id, 10, '0') into flag;
    select sum(pay_money) from BankManage_payment where fk_loan_id = LPAD(loan_id, 10, '0') into money;
    if flag = 0 then
        return 0;
    else 
        return money;
    end if;
end //
delimiter ;