-- MySQL Basic Query Practice Assessment
-- Questions Only
-- Topics: Database, USE, CREATE TABLE, DESC, INSERT, SELECT, WHERE, UPDATE

-- ============================================================
-- SECTION 1: DATABASE OPERATIONS
-- ============================================================

-- Q1. Create a database named employee_db.
create database employee_db;

-- Q2 switch to employee_db
use employee_db;


-- ============================================================
-- SECTION 2: CREATE TABLE
-- ============================================================

-- Q6. Inside employee_db, create a table named employee with:
--     id        -> integer, auto increment, primary key
--     name      -> varchar(100), cannot be NULL
--     age       -> integer, cannot be NULL
--     salary    -> float, cannot be NULL
--     department -> enum('hr','it','sales','finance') with default 'it'

create table employee_details(

     id int auto_increment primary key,
     name varchar(100) not null,
     age int not null,
     salary float not null,
     department enum("hr","it","sales","finace") default "it"
);

-- ============================================================
-- SECTION 3: DESCRIBING TABLES

desc employee_details;
-- ============================================================

-- Q11. Write a query to display the structure of the employee table.






-- ============================================================
-- SECTION 4: INSERT RECORDS
-- ============================================================

-- Q16. Insert the following employee into the employee table:
--      name: Arun
--      age: 25
--      salary: 30000
--      department: it

insert into employee_details (name,age,salary,department) values ("Arun",25,30000,"it");
insert into employee_details (name,age,salary,department) values ("jeepsi",25,30000,"hr");
-- Q17. Insert the following employee into the employee table:
--      name: Meera
--      age: 28
--      salary: 42000
--      department: hr

insert into employee_details (name,age,salary,department) values ("Meera",28,42000,"hr");
insert into employee_details (name,age,salary,department) values ("jhony",28,42000,"finace");
-- Q18. Insert the following employee into the employee table:
--      name: Rahul
--      age: 32
--      salary: 55000
--      department: finance

insert into employee_details (name,age,salary,department) values ("Rahul",24,31000.40,"finace");
insert into employee_details (name,age,salary,department) values ("jhnothan",28,42000,"hr");
-- Q19. Insert the following patient into the patient table:
--      name: Anu
--      age: 35
--      disease: Fever
--      fee: 500

insert into employee_details (name,age,salary,department) values ("Anu",24,31000.40,"finace");
insert into employee_details (name,age,salary,department) values ("alex",22,31000.40,"finace");
-- ============================================================
-- SECTION 5: SELECT RECORDS
-- ============================================================

-- Q26. Write a query to display all records from the employee table.

select * from employee_details;

-- write name and salary

select name,salary from employee_details; 

-- ============================================================
-- SECTION 6: FILTERING USING WHERE
-- ============================================================

-- Q31. Display the employee whose id is 2.

select * from employee_details where id = 2;

-- Q32. Display the employee whose name is 'Arun'.
select * from employee_details where name = "Arun";

-- Q33. Display all employees whose age is 30.
select * from employee_details where age = 30;

-- Q34. Display all employees whose department is 'it'.
select * from employee_details where department = "it";

-- Q35. Display all employees whose salary is 50000.
select * from employee_details where salary = 50000;




-- ============================================================
-- SECTION 7: UPDATE RECORDS
-- ============================================================

-- Q47. Change the salary of the employee with id 1 to 35000.
update employee_details set salary = 50000 where id=2;

-- Q48. Change the department of the employee with id 2 to 'sales'.
update employee_details set department = "sales" where id= 2;

-- Q49. Change the age of the employee with id 3 to 35.
update employee_details set age = 35 where id= 3;

-- Q50. Change both salary and department of the employee with id 1:
--      salary = 40000
--      department = 'finance'
update employee_details set salary = 40000 and department = "finance" where id= 1;

delete from employee_details where id=5;

-- select employee > 34000

select * from employee_details where salary > 34000;

-- display employee whose salary in range of 30k to 45k
select * from employee_details where salary >= 30000 and salary <= 45000; 

-- operators <>,<=,>=,!=,<>

-- dispaly employee record 	whose age not 30
select * from employee_details where age != 30;

-- multiple condition evalution and,or,not

-- display empolyee records having salary > 35000 and department it

select * from employee_details where salary > 35000 and department = "it";

-- display emplyee whose deparment either hr or it 

select * from employee_details where department = "hr" or department ="it";

-- using in python membership operator helping to identify
select * from employee_details where department in ("hr","it");

-- display empolyee whose not working in it,hr
-- using to not in 	
select * from employee_details where department not in ("hr","it");

-- between
-- select employee whose salary in range 30k - 45k
select * from employee_details where salary between 30000 and 45000; 

-- order by 
-- using arange order vise seting
select * from employee_details order by salary;
-- desenting method using desc
select * from employee_details order by salary desc;

-- age asending and desending
-- age asending order
select * from employee_details order by age;
-- age desending order
select * from employee_details order by age desc;

-- limit , offset
-- limit using to limitaion offset using skip
-- employee with highest age
select * from empolyee_details order by age desc limit 1;
-- employee with second highest age
select * from employee_details order by age desc limit 1 offset 1;
-- employee with highest salary
select * from employee_details order by salary desc limit 1;
-- employee with seconfd highest salary
select * from employee_details order by salary desc limit 1 offset 1;

-- agregate function max,min,sum,count,avg
select count(*) from employee_details;
select sum(salary) from employee_details;
select max(salary) from employee_details;
select min(salary) from employee_details;
select avg(salary) from employee_details;

-- subquery , nexted query
-- write a query to display highest salareid employee
select * from employee_details where salary = (select max(salary) from employee_details);
-- lowest salary
select * from employee_details where salary = (select min(salary) from emoloyee_details);

-- highest age
select * from employee_details where age = (select max(age) from employee_details);
-- lowest age
select * from employee_details where age = (select min(age) from employee_details);

-- remove to duplicate
select distinct department from employee_details;

update employee_details set name = "alex" where id= 1;
update employee_details set department = "hr" where id= 2;

-- using to "group by" methods 	
select department,count(*) from employee_details group by department;
-- using to as total change the tabile name (sum -> total) 
select department,sum(salary) as total from employee_details group by department order by total desc;

-- deparment with most number of employees
select department ,count(*) as mostemployee from employee_details group by department order by mostemployee desc limit 1;

-- display deparment more than 1 employee
-- using to "having" purpose is condition writing in "group by" statement
select department, count(*) as count from employee_details group by department having count > 1;

