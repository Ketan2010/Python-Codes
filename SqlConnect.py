#pip install mysql-connector
import mysql.connector

#to make connections with mysql
conn=mysql.connector.connect(user='root',password='password',host='localhost')
mycursor=conn.cursor()

#create new database "python"
mycursor.execute("create database python")

#make use of created database
mycursor.execute("use python")

#create table customer in python database
mycursor.execute("create table customer(custId int primary key,CustName varchar(10),Address varchar(40),CustNo varchar(10));")

#ask user for inputs to be filled in customer table
id=int(input("enter id:"))
name=input("enter name:")
address=input("enter address:")
cont=input("enter contact no:")

#insert the values entered by user in customer table
mycursor.execute("insert into customer values(%s,%s,%s,%s)",(id,name,address,cont))

#below line is necceessary to make changes in cutomer table
conn.commit()
mycursor.execute("select * from customer")

#create list which will contains rows of table
mylist=mycursor.fetchall()

#print table data present in list
for x in mylist:
    print(x)