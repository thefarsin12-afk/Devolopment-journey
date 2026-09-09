create database road_issue_db;
use road_issue_db;

-- [id,title,location,posted_by,status(unsolved,solved)]

create table issue_(
   id int auto_increment primary key,
   title varchar(200) not null,
   location varchar(200) not null,
   posted_by varchar(150) not null,
   status enum("unsolved","solved")
);