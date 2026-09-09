create database todo_db;

use todo_db;

create table user_1(
  id int auto_increment primary key,
  name varchar(200) not null,
  email varchar(150) not null
);

insert into user_1(name,email) values("alexi","alexi@gmail.com");
insert into user_1(name,email) values("felix","alexi@gmail.com");
insert into user_1(name,email) values("jhon","alexi@gmail.com");

create table todo_1(

  id int auto_increment primary key,
  title varchar(200) not null,
  status_1 enum ("in progress","complted"),
  user_id int not null
);

insert into todo_1(title,status_1,user_id) values("send email","in progress",1);
insert into todo_1(title,status_1,user_id) values("buy grocery","complted",2);
insert into todo_1(title,status_1,user_id) values("finsh work","in progress",3);
insert into todo_1(title,status_1,user_id) values("complte task","complted",4);
insert into todo_1(title,status_1,user_id) values("send email","complted",5);

select * from user_1;
select * from todo_1;



