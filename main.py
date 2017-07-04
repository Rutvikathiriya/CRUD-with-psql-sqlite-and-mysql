# -*- coding : utf-8 -*-
import sys
import db_query 

def create_table():
    data.create()

def insert():
    id = raw_input("Enter id : ")
    name = raw_input("Enter name : ")
    city = raw_input("Enter city : ")
    phone = raw_input("Enter phone : ")
    data.insert(id,name,city,phone)

def delete():
    id = raw_input("Enter id You want to delete : ")
    data.delete(id)

def update():
    id = raw_input("Enter id for updated : ")
    name = raw_input("Enter updated name : ")
    city = raw_input("Enter updated city : ")
    phone = raw_input("Enter updated phone : ")
    data.update(id,name,city,phone)

def add_col():
    col = raw_input("Enter a coloumn : ")
    data.addcolumn(col)

def del_col():
    col = raw_input("Enter a column to del : ")
    data.deletecol(col)

def delete_table():
    delcol = raw_input("Enter table name to delete : ")
    data.delete_table1(delcol)

def list_table():
    print "1.sqlite\n2.Mysql\n3.postgresql\n"
    user = raw_input("Enter database : ")
    if user == '1':
        data.list_table_sqlite()
    elif user == '2':
        data.list_table_mysql()
    elif user == '3':
        data.list_table_postgresql()


def list_database():
    print "1.sqlite\n2.Mysql\n3.postgresql\n"
    user = raw_input("Enter database : ")
    if user == '1':
        data.list_db_sqlite()
    elif user == '2':
        data.list_db_mysql()
    elif user == '3':
        data.list_db_postgresql()

def create_db():
    print "1.sqlite\n2.Mysql\n3.postgresql\n"
    user = raw_input("Enter database : ")
    if user == '1':
        data.create_db_sqlite()
    elif user == '2':
        data.create_db_mysql()
    elif user == '3':
        data.create_db_postgresql()


def opration():
    print "1.Create Databse"
    print "2.List Of Table"
    print "3.List Of Database"
    print "4 Create Table"
    print "5.Read Data"
    print "6.Insert Data"
    print "7.Update Data"
    print "8.Delete Data"
    print "9.Add coloumn"
    print "10.Delete coloumn"
    print "11.Delete Table"
    print "12.Quit"
    user_opr = raw_input("Which operations you want to perform : ")
    
    if user_opr == "1":
        create_db()
        opration()
    elif user_opr == "2":
        list_table()
        opration()
    elif user_opr == "3":
        list_database()
        opration()
    elif user_opr == "4":
        create_table()
        opration()
    elif user_opr == "5":
        data.retrive()
        opration()
    elif user_opr == "6":
        insert()
        opration()
    elif user_opr == "7":
        update()
        opration()
    elif user_opr == "8":
        delete()
        opration()
    elif user_opr == "9":
        add_col()
        opration()
    elif user_opr == "10":
        del_col()
        opration()
    elif user_opr == "11":
        delete_table()
        opration()
    elif user_opr == "12":
        quit()


def choice():
    print "---------------"
    print "1.Sqlite"
    print "2.Mysql"
    print "3.Postgresql"
    print "4.Exit"
    print "---------------"
    selectDB = raw_input("Choose Database:")

    if selectDB == '4':
        exit()
    elif selectDB:
        global data
        data = db_query.DataBase(selectDB)
        data.create()
        opration()

choice()
