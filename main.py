# -*- coding : utf-8 -*-
import sys
import db_query 

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

def list_table():
    print "1.sqlite\n2.Mysql\n3.postgresql\n"
    user = raw_input("Enter database : ")
    if user == '1':
        data.list_table_sqlite()
    elif user == '2':
        data.list_table_mysql()
    elif user == '3':
        data.list_table_postgresql()



def opration():
    print "1.Insert "
    print "2.Read data "
    print "3.Update "
    print "4.Delete "
    print "5.Add coloumn"
    print "6.Delete coloumn"
    print "7.List Table"
    print "8.Quit"
    user_opr = raw_input("Which operations you want to perform : ")
    if user_opr == "1":
        insert()
        opration()
    elif user_opr == "2":
        data.retrive()
        opration()
    elif user_opr == "3":
        update()
        opration()
    elif user_opr == "4":
        delete()
        opration()
    elif user_opr == "5":
        add_col()
        opration()
    elif user_opr == "6":
        del_col()
        opration()
    elif user_opr == "7":
        list_table()
        opration()
    elif user_opr == "8":
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