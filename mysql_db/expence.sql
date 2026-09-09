create database expence_db;
show databases;
use expence_db;

create table expence1(
  
     id int primary key auto_increment,
     owner_name varchar(150) not null,
     amount int not null,
     date_details date not null,
     category varchar(100) not null,
     payment_method enum("upi","card","cash","bank transfer") default "upi"
     
);

desc expence1;

-- owner_name,amount,date_details,category,payment_method

insert into expence1 (owner_name,amount,date_details,category,payment_method)
values ("Farsin",180,"2026-08-01","food","upi");

insert into expence1 (owner_name,amount,date_details,category,payment_method)
values ("Anjali",450,"2026-08-01","shopping","card");

insert into expence1 (owner_name,amount,date_details,category,payment_method) 
values ("Rahul",850,"2026-08-01","fuel","cash");

insert into expence1 (owner_name,amount,date_details,category,payment_method) 
values ("Nithin",250,"2026-08-01","food","cash");

insert into expence1 (owner_name,amount,date_details,category,payment_method) 
values ("Meera",3000,"2026-08-01","rent","bank transfer");

select * from expence1;

select * from expence1 where id=2;

update expence1 set owner_name = "felixa", amount = 2500 where id = 2;

select * from expence1 where id=2
