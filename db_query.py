#!/usr/bin/python
# -*- coding : utf-8 -*-

import db_config,sys,sqlite3
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

class DataBase:
    conn = 0
    db = ""

    def __init__(self,user):
        if user == "1":
            self.conn = db_config.connection_mysql()
        elif user == "2":
            self.conn = db_config.connection_sqlite()
        elif user == "3":
            self.conn = db_config.connection_postgresql()

#------------------Create Table------------------------

    def create(self):
            cur = self.conn.cursor()
            cur.execute("DROP TABLE IF EXISTS employ")
            cur.execute("CREATE TABLE employ(Id INT,Name VARCHAR(25),City TEXT,Phone INT)")
            print "New table is created"
            self.conn.commit()

#------------------Create Database-------------------------

    def create_db_mysql(self):
        self.conn = db_config.connection_mysql()
        cur = self.conn.cursor()
        name = raw_input ("Enter name for Database")
        cur.execute("SET sql_notes = 0; ")
        cur.execute("CREATE DATABASE IF NOT EXISTS " + name + ";")
        print "Database Created Successfully"
        self.conn.commit()

    def create_db_sqlite(self):
        self.conn = db_config.connection_sqlite()
        name = raw_input("Enter a name of new database : ")
        sqlite3.connect(name + '.db')
        print "new database create"
        self.conn.commit()

    def create_db_postgresql(self):
        cur = self.conn.cursor()
        name = raw_input("Enter a name of new database : ")
        self.conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cur.execute('CREATE DATABASE ' + name)
        print "new database create"
        self.conn.commit()

#------------------List of Tables-------------------------

    def list_table_mysql(self):
        self.conn = db_config.connection_mysql()
        cur = self.conn.cursor()
        cur.execute('SHOW TABLES')
        rows = cur.fetchall()
        print "list of table : "
        for row in rows:
            print row

    def list_table_sqlite(self):
        self.conn = db_config.connection_sqlite()
        cur = self.conn.cursor()
        cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
        rows = cur.fetchall()
        print "list of table : "
        for row in rows:
            print row

    def list_table_postgresql(self):
        self.conn = db_config.connection_postgresql()
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM information_schema.tables WHERE table_type = 'BASE TABLE' AND table_schema = 'public' ORDER BY table_type, table_name")
        rows = cur.fetchall()
        print "list of table : "
        for row in rows:
            print row[2]


#------------------List of Databases------------------------


    def list_db_sqlite(self):
        self.conn = db_config.connection_sqlite()
        cur = self.conn.cursor()
        cur.execute('PRAGMA database_list;')
        rows = cur.fetchall()
        for row in rows:
            print row[2]

    def list_db_mysql(self):
        self.conn = db_config.connection_mysql()
        cur = self.conn.cursor()
        cur.execute('SHOW DATABASES')
        rows = cur.fetchall()
        for row in rows:
            print row

    def list_db_postgresql(self):
        self.conn = db_config.connection_postgresql()
        cur = self.conn.cursor()
        cur.execute('SELECT datname FROM pg_database WHERE datistemplate = false;')
        rows = cur.fetchall()
        for row in rows:
            print row

#-------------------Read Data-----------------------

    def retrive(self):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM employ")
        for i in range(cur.rowcount):
            row = cur.fetchone()
            print row

#-------------------Insert Data-----------------------

    def insert(self,*args):
        try:
            cur = self.conn.cursor()
            id = args[0]
            name = args[1]
            city = args[2]
            phone = args[3]
            cur.execute("""INSERT INTO employ VALUES (%s,'%s', '%s', %s);"""% (id,name,city,phone))
            print "Record inserted into Table"
            self.conn.commit()
        except Warning, e:
            pass

#-------------------Update Data-----------------------

    def update(self,*args):
        cur = self.conn.cursor()
        id = args[0]
        name = args[1]
        city = args[2]
        phone = args[3]
        cur.execute("UPDATE employ SET name = %s, city = %s, phone = %s WHERE id = %s",(name,city,phone,id))
        print "Record Updated in Table"
        self.conn.commit()

#-------------------Delete Data-----------------------

    def delete(self,*args):
        cur = self.conn.cursor()
        i = args[0]
        try:
            cur.execute("DELETE FROM employ WHERE Id = %s",(i,))
            print "Record deleted"
        except Exception as e:
            print "Record with the given id not found"

#-------------------Add Column-----------------------

    def addcolumn(self, *args):
        cur = self.conn.cursor()
        cur.execute("ALTER TABLE employ ADD COLUMN " + args[0] + " VARCHAR(15);")
        self.conn.commit()
        print "Column is added"

#------------------Delete Column----------------------

    def deletecol(self, *args):
        cur = self.conn.cursor()
        cur.execute("ALTER TABLE employ DROP COLUMN " + args[0] )
        self.conn.commit()
        print "Column is deleted"

#-------------------Delete Table----------------------

    def delete_table1(self,*args):
        cur = self.conn.cursor()
        cur.execute("DROP TABLE " + args[0])
        self.conn.commit()
        print "Table is Deleted"
