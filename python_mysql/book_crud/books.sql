create database books_db;
use books_db;

create table book(
 id int auto_increment primary key,
 title varchar(200) not null,
 author varchar(200) not null,
 price int not null
);

select * from book;