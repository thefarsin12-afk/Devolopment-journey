create database movie_dt;
show databases;
use movie_dt;

-- id,title,year,run_time,rating,genre

create table movie(
    
   id int primary key auto_increment,
   title varchar(200) not null,
   year varchar (20) not null,
   run_time int,
   rating decimal(2,1) not null,
   genre enum("action","comedy","thriller","horror") default "action"
);

desc movie;

-- creating to tabile structure insert into tabile name col() val() get()

insert into movie (title,year,run_time,rating,genre) values ("abcd",2006,120,8.6,"comedy");
insert into movie (title,year,run_time,rating,genre) values ("jhonwick",2024,140,8.9,"action");
insert into movie (title,year,run_time,rating,genre) values ("obsession",2025,130,8.1,"thriller");
insert into movie (title,year,run_time,rating,genre) values ("bheeshma",2023,120,7.8,"action");
insert into movie (title,year,run_time,rating,genre) values ("arrival",2019,120,7.4,"thriller");
s
-- using to list all method syntax
select * from movie;

-- using list details retrive
select * from movie where id = 2;

-- updating method put
update movie set title = "balan the boy", run_time = 150 where id = 3;
select * from movie where id = 3;




