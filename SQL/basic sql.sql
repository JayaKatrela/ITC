-- Create Database
create database ITC;

-- To use database
use ITC;

-- create table
create table Department(
	Dept_ID int primary key,
    Dept_Name varchar(50));
    
create table Employee (
	Emp_ID int primary key,
    Emp_Name varchar(100),
    Dept_ID int,
    Salary decimal(10,2),
    foreign key(Dept_ID) references Department(Dept_ID));
    
create table Project (
	Project_ID int primary key,
    Project_Name varchar(100),
    Dept_ID int,
    foreign key(Dept_ID) references Department(Dept_ID));
    
-- insert data into table
insert into Department(Dept_ID, Dept_Name)
values(1,'Engineering'),(2,'Sales'),(3,'HR');

insert into Employee(Emp_ID, Emp_Name, Dept_ID, Salary)
values(101,'Alice',1,75000.00),(104,'David',3,60000.00);

insert into Project(Project_ID, Project_Name, Dept_ID)
values(1,'AI Development',1),(2,'Customer Support',2);

-- SQL Opertation
-- ALTER use for adding a column to the table
alter table Employee
add column Joining_Date date;

-- UPDATE use for updating data into the table
update Employee
set Salary=85000.00
where EMP_ID=102;

-- Delete use for deleting data into table
delete from Employee
where Emp_ID=104;
