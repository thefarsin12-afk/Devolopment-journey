create database course_db;

use course_db;

-- course (id,title,fee,duration)
create table course_1(
  id int auto_increment primary key,
  title varchar(200) unique not null,
  fee decimal(8,2) not null,
  duration varchar(100) not null
);

insert into course_1 (title,fee,duration) values ("django",65000,"6-month");
insert into course_1 (title,fee,duration) values ("mearn",75000,"6-month");
insert into course_1 (title,fee,duration) values ("DS",85000,"6-month");

-- batch (id,title,head_count,course_id)
create table batch_1(
  id int auto_increment primary key,
  title varchar(200) unique not null,
  head_count int not null,
  course_id int not null
);
insert into batch_1 (title,head_count,course_id) values ("pydjjune", 40,1);
insert into batch_1 (title,head_count,course_id) values ("pydjjulye", 44,1);
insert into batch_1 (title,head_count,course_id) values ("msjune", 40,2);
insert into batch_1 (title,head_count,course_id) values ("msaug", 40,2);
insert into batch_1 (title,head_count,course_id) values ("swtjune", 40,5);

select * from course_1;
select * from batch_1;

select course_1.title ,course_1.fee,batch_1.title,batch_1.head_count from course_1 left join batch_1 on course_1.id = batch_1.id ;
select course_1.title ,course_1.fee,batch_1.title,batch_1.head_count from course_1 inner join batch_1 on course_1.id = batch_1.id ;
select course_1.title ,course_1.fee,batch_1.title,batch_1.head_count from course_1 right join batch_1 on course_1.id = batch_1.id ;