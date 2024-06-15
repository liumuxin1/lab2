#分行
INSERT INTO BankManage_bank (title,city,assset) VALUES ('合肥分行','合肥',0.0);
INSERT INTO BankManage_bank (title,city,assset) VALUES ('上海分行','上海',0.0);
INSERT INTO BankManage_bank (title,city,assset) VALUES ('北京分行','北京',0.0);

#各个分行的部门
INSERT INTO BankManage_department (Depart_ID,fk_bank_id,title,dtype) VALUES ('BS001','合肥分行','业务部','BS');
INSERT INTO BankManage_department (Depart_ID,fk_bank_id,title,dtype) VALUES ('HR001','合肥分行','人力资源部','HR');
INSERT INTO BankManage_department (Depart_ID,fk_bank_id,title,dtype) VALUES ('Tech001','合肥分行','技术部','Tech');
INSERT INTO BankManage_department (Depart_ID,fk_bank_id,title,dtype) VALUES ('A&M001','合肥分行','会计管理部','A&M');

INSERT INTO BankManage_department (Depart_ID,fk_bank_id,title,dtype) VALUES ('BS002','上海分行','业务部','BS');
INSERT INTO BankManage_department (Depart_ID,fk_bank_id,title,dtype) VALUES ('HR002','上海分行','人力资源部','HR');
INSERT INTO BankManage_department (Depart_ID,fk_bank_id,title,dtype) VALUES ('Tech002','上海分行','技术部','Tech');
INSERT INTO BankManage_department (Depart_ID,fk_bank_id,title,dtype) VALUES ('A&M002','上海分行','会计管理部','A&M');

INSERT INTO BankManage_department (Depart_ID,fk_bank_id,title,dtype) VALUES ('BS003','北京分行','业务部','BS');
INSERT INTO BankManage_department (Depart_ID,fk_bank_id,title,dtype) VALUES ('HR003','北京分行','人力资源部','HR');
INSERT INTO BankManage_department (Depart_ID,fk_bank_id,title,dtype) VALUES ('Tech003','北京分行','技术部','Tech');
INSERT INTO BankManage_department (Depart_ID,fk_bank_id,title,dtype) VALUES ('A&M003','北京分行','会计管理部','A&M');


# 员工
INSERT INTO BankManage_employee (ID_card,fk_bank_id,fk_department_id,name,phone,address,entry_date) VALUES ('341302199004058330','合肥分行','1','许浩然','42651711695','CUST042','2019-12-09');
INSERT INTO BankManage_employee (ID_card,fk_bank_id,fk_department_id,name,phone,address,entry_date) VALUES ('652123199507243911','合肥分行','1','水雨桐','05341125923','USCT032','2013-05-28');
INSERT INTO BankManage_employee (ID_card,fk_bank_id,fk_department_id,name,phone,address,entry_date) VALUES ('620104196001066399','合肥分行','1','杨语汐','66239618788','UCST029','2011-09-18');
INSERT INTO BankManage_employee (ID_card,fk_bank_id,fk_department_id,name,phone,address,entry_date) VALUES ('542326199706145470','合肥分行','1','尤欣怡','48023739048','UTSC066','2021-10-19');
INSERT INTO BankManage_employee (ID_card,fk_bank_id,fk_department_id,name,phone,address,entry_date) VALUES ('530325197006219978','合肥分行','1','陈可欣','45646970011','USCT036','2011-07-04');
INSERT INTO BankManage_employee (ID_card,fk_bank_id,fk_department_id,name,phone,address,entry_date) VALUES ('510303198408134208','合肥分行','2','何梓涵','29549152093','USTC035','2012-02-09');
INSERT INTO BankManage_employee (ID_card,fk_bank_id,fk_department_id,name,phone,address,entry_date) VALUES ('522229198503252159','合肥分行','2','郎宇航','60324086184','CTUS089','2011-05-08');
INSERT INTO BankManage_employee (ID_card,fk_bank_id,fk_department_id,name,phone,address,entry_date) VALUES ('140624197904201654','合肥分行','2','凤浩宇','29724260615','CSTU004','2017-07-07');
INSERT INTO BankManage_employee (ID_card,fk_bank_id,fk_department_id,name,phone,address,entry_date) VALUES ('130124197007193608','合肥分行','2','姜浩宇','00547568588','TCUS078','2016-05-27');
INSERT INTO BankManage_employee (ID_card,fk_bank_id,fk_department_id,name,phone,address,entry_date) VALUES ('450601196812014177','合肥分行','2','蒋浩宇','83422385913','SCUT030','2016-11-09');
INSERT INTO BankManage_employee (ID_card,fk_bank_id,fk_department_id,name,phone,address,entry_date) VALUES ('371327196412185020','合肥分行','3','卫一诺','62196238591','UTSC051','2017-05-02');
INSERT INTO BankManage_employee (ID_card,fk_bank_id,fk_department_id,name,phone,address,entry_date) VALUES ('360202197508122357','合肥分行','3','金依诺','12402237541','UCST011','2016-04-19');
INSERT INTO BankManage_employee (ID_card,fk_bank_id,fk_department_id,name,phone,address,entry_date) VALUES ('130822198510172214','合肥分行','3','戚梓涵','33183594699','TUCS027','2011-06-08');
INSERT INTO BankManage_employee (ID_card,fk_bank_id,fk_department_id,name,phone,address,entry_date) VALUES ('211281199211203183','合肥分行','3','赵语桐','36134756109','TSCU019','2018-06-06');
INSERT INTO BankManage_employee (ID_card,fk_bank_id,fk_department_id,name,phone,address,entry_date) VALUES ('542233196309128559','合肥分行','3','王宇辰','23240582059','TCUS009','2021-11-30');
INSERT INTO BankManage_employee (ID_card,fk_bank_id,fk_department_id,name,phone,address,entry_date) VALUES ('130703199612194713','合肥分行','4','章子墨','41743145878','SCUT072','2010-06-23');
INSERT INTO BankManage_employee (ID_card,fk_bank_id,fk_department_id,name,phone,address,entry_date) VALUES ('411121198504258488','合肥分行','4','陶浩宇','98337704739','CUST057','2011-11-08');
INSERT INTO BankManage_employee (ID_card,fk_bank_id,fk_department_id,name,phone,address,entry_date) VALUES ('230521197708022269','合肥分行','4','王梓涵','58606900030','TSCU081','2012-11-23');
INSERT INTO BankManage_employee (ID_card,fk_bank_id,fk_department_id,name,phone,address,entry_date) VALUES ('653001196011075209','合肥分行','4','褚梦瑶','04741213867','SUCT064','2018-02-06');
INSERT INTO BankManage_employee (ID_card,fk_bank_id,fk_department_id,name,phone,address,entry_date) VALUES ('131028199910317945','合肥分行','4','郑浩宇','95911891176','STCU024','2017-04-12');
INSERT INTO BankManage_employee (ID_card,fk_bank_id,fk_department_id,name,phone,address,entry_date) VALUES ('362429199711096280','上海分行','5','奚浩然','22902814552','TCUS053','2019-07-10');
INSERT INTO BankManage_employee (ID_card,fk_bank_id,fk_department_id,name,phone,address,entry_date) VALUES ('420503198911214204','上海分行','5','姜亦宸','89540209292','UTSC025','2017-10-26');
INSERT INTO BankManage_employee (ID_card,fk_bank_id,fk_department_id,name,phone,address,entry_date) VALUES ('120110199709302724','上海分行','5','俞浩然','22123005326','UTCS030','2014-08-08');
INSERT INTO BankManage_employee (ID_card,fk_bank_id,fk_department_id,name,phone,address,entry_date) VALUES ('372922198605079348','上海分行','5','韦浩然','71000895410','UTCS038','2012-02-23');
INSERT INTO BankManage_employee (ID_card,fk_bank_id,fk_department_id,name,phone,address,entry_date) VALUES ('22072419640104191X','上海分行','5','李语桐','54202464582','USTC014','2012-11-14');
INSERT INTO BankManage_employee (ID_card,fk_bank_id,fk_department_id,name,phone,address,entry_date) VALUES ('37108119681203221X','上海分行','6','昌梓涵','34962559557','CUTS045','2015-11-09');
INSERT INTO BankManage_employee (ID_card,fk_bank_id,fk_department_id,name,phone,address,entry_date) VALUES ('340604198503224739','上海分行','6','华可欣','05772372990','CSUT035','2020-05-22');
INSERT INTO BankManage_employee (ID_card,fk_bank_id,fk_department_id,name,phone,address,entry_date) VALUES ('370202196210131346','上海分行','6','赵依诺','30674631567','CTSU004','2010-08-23');
INSERT INTO BankManage_employee (ID_card,fk_bank_id,fk_department_id,name,phone,address,entry_date) VALUES ('51343519630927319X','上海分行','6','葛欣怡','12611065108','TUCS076','2015-01-20');
INSERT INTO BankManage_employee (ID_card,fk_bank_id,fk_department_id,name,phone,address,entry_date) VALUES ('370902198109238349','上海分行','6','潘一诺','85628791881','UCTS010','2017-12-05');
INSERT INTO BankManage_employee (ID_card,fk_bank_id,fk_department_id,name,phone,address,entry_date) VALUES ('362322197112131460','上海分行','7','冯梓豪','61279718977','STCU050','2018-05-02');
INSERT INTO BankManage_employee (ID_card,fk_bank_id,fk_department_id,name,phone,address,entry_date) VALUES ('220302198902069645','上海分行','7','赵雨桐','46929442417','CTUS010','2013-04-02');
INSERT INTO BankManage_employee (ID_card,fk_bank_id,fk_department_id,name,phone,address,entry_date) VALUES ('330784196802227880','上海分行','7','韦子墨','46778873948','USTC031','2020-08-09');
INSERT INTO BankManage_employee (ID_card,fk_bank_id,fk_department_id,name,phone,address,entry_date) VALUES ('372300199003175010','上海分行','7','花梓豪','33148094486','STUC038','2015-07-21');
INSERT INTO BankManage_employee (ID_card,fk_bank_id,fk_department_id,name,phone,address,entry_date) VALUES ('370923198002114524','上海分行','7','孔宇辰','84619040517','USTC052','2014-02-08');
INSERT INTO BankManage_employee (ID_card,fk_bank_id,fk_department_id,name,phone,address,entry_date) VALUES ('330201198903028582','上海分行','8','昌语桐','21871760667','USTC010','2014-08-30');
INSERT INTO BankManage_employee (ID_card,fk_bank_id,fk_department_id,name,phone,address,entry_date) VALUES ('652926198410244529','上海分行','8','柏欣妍','33408893012','UTCS078','2019-09-01');
INSERT INTO BankManage_employee (ID_card,fk_bank_id,fk_department_id,name,phone,address,entry_date) VALUES ('513334198402162854','上海分行','8','葛宇轩','72190278659','TUCS058','2010-09-07');
INSERT INTO BankManage_employee (ID_card,fk_bank_id,fk_department_id,name,phone,address,entry_date) VALUES ('360421198901124994','上海分行','8','花奕辰','56976089490','TUSC032','2014-09-27');
INSERT INTO BankManage_employee (ID_card,fk_bank_id,fk_department_id,name,phone,address,entry_date) VALUES ('420682196312251742','上海分行','8','孔浩然','90225003587','TUCS055','2015-02-27');
INSERT INTO BankManage_employee (ID_card,fk_bank_id,fk_department_id,name,phone,address,entry_date) VALUES ('500102199808226975','北京分行','9','马梓涵','99948317258','CSUT050','2017-11-06');
INSERT INTO BankManage_employee (ID_card,fk_bank_id,fk_department_id,name,phone,address,entry_date) VALUES ('371502199904103324','北京分行','9','卫可欣','31858621995','CTUS070','2010-01-13');
INSERT INTO BankManage_employee (ID_card,fk_bank_id,fk_department_id,name,phone,address,entry_date) VALUES ('410703196111112795','北京分行','9','俞依诺','16732099363','UTCS086','2014-07-24');
INSERT INTO BankManage_employee (ID_card,fk_bank_id,fk_department_id,name,phone,address,entry_date) VALUES ('130106197809268453','北京分行','9','沈雨桐','54593197400','UTCS035','2015-09-24');
INSERT INTO BankManage_employee (ID_card,fk_bank_id,fk_department_id,name,phone,address,entry_date) VALUES ('420703198012204142','北京分行','9','俞亦宸','14161163155','CUST004','2020-07-20');
INSERT INTO BankManage_employee (ID_card,fk_bank_id,fk_department_id,name,phone,address,entry_date) VALUES ('140501199403146369','北京分行','10','褚亦辰','36431388342','CUTS077','2019-05-27');
INSERT INTO BankManage_employee (ID_card,fk_bank_id,fk_department_id,name,phone,address,entry_date) VALUES ('320302196703154980','北京分行','10','邹浩宇','25662670077','UTCS045','2020-10-05');
INSERT INTO BankManage_employee (ID_card,fk_bank_id,fk_department_id,name,phone,address,entry_date) VALUES ('14050019600318741X','北京分行','10','赵语汐','51010836729','CTUS093','2011-02-05');
INSERT INTO BankManage_employee (ID_card,fk_bank_id,fk_department_id,name,phone,address,entry_date) VALUES ('500384197501206263','北京分行','10','秦欣怡','30380518113','CUTS069','2011-01-07');
INSERT INTO BankManage_employee (ID_card,fk_bank_id,fk_department_id,name,phone,address,entry_date) VALUES ('350205199609041296','北京分行','10','苏欣怡','83109414975','CUTS099','2013-12-18');
INSERT INTO BankManage_employee (ID_card,fk_bank_id,fk_department_id,name,phone,address,entry_date) VALUES ('370800197608155764','北京分行','11','曹亦宸','90251822409','TSCU074','2012-02-24');
INSERT INTO BankManage_employee (ID_card,fk_bank_id,fk_department_id,name,phone,address,entry_date) VALUES ('130821196503299932','北京分行','11','葛亦辰','34299878363','UCTS084','2016-04-16');
INSERT INTO BankManage_employee (ID_card,fk_bank_id,fk_department_id,name,phone,address,entry_date) VALUES ('610728196112065614','北京分行','11','鲁宇航','23893047582','SUTC074','2011-12-31');
INSERT INTO BankManage_employee (ID_card,fk_bank_id,fk_department_id,name,phone,address,entry_date) VALUES ('370400197811209244','北京分行','11','俞浩然','90327503262','SUCT059','2012-04-03');
INSERT INTO BankManage_employee (ID_card,fk_bank_id,fk_department_id,name,phone,address,entry_date) VALUES ('362428196412061379','北京分行','11','华宇辰','63939302962','CTUS066','2017-02-04');
INSERT INTO BankManage_employee (ID_card,fk_bank_id,fk_department_id,name,phone,address,entry_date) VALUES ('372924196603073333','北京分行','12','窦宇轩','48333379415','CUTS092','2017-03-24');
INSERT INTO BankManage_employee (ID_card,fk_bank_id,fk_department_id,name,phone,address,entry_date) VALUES ('652825196704082747','北京分行','12','陶可欣','59007502114','TUCS008','2016-01-16');
INSERT INTO BankManage_employee (ID_card,fk_bank_id,fk_department_id,name,phone,address,entry_date) VALUES ('230601198609229760','北京分行','12','何子墨','59757068587','TUSC029','2021-04-21');
INSERT INTO BankManage_employee (ID_card,fk_bank_id,fk_department_id,name,phone,address,entry_date) VALUES ('513227199510254858','北京分行','12','尤奕辰','82798799420','UTSC045','2014-07-04');
INSERT INTO BankManage_employee (ID_card,fk_bank_id,fk_department_id,name,phone,address,entry_date) VALUES ('350211196103081104','北京分行','12','沈欣怡','76608039224','UCTS099','2014-10-06');