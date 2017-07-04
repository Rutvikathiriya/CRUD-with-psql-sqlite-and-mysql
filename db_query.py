#!/usr/bin/python
# -*- coding : utf-8 -*-

import db_config,sys

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

    def create(self):
            cur = self.conn.cursor()
            cur.execute("DROP TABLE IF EXISTS employ")
            cur.execute("CREATE TABLE employ(Id INT,Name VARCHAR(25),City TEXT,Phone INT)")
            print "New table is created"
            self.conn.commit()

    def insert(self,*args):
        try:
            cur = self.conn.cursor()
            id = args[0]
            name = args[1]
            city = args[2]
            phone = args[3]

            cur.execute("""INSERT INTO employ VALUES (%s,'%s', '%s', %s);"""%(id,name,city,phone))
            print "Record inserted into Table"
            self.conn.commit()
        except Warning, e:
            pass

    def retrive(self):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM employ")

        for i in range(cur.rowcount):
            row = cur.fetchone()
            print row

    def update(self,*args):
        cur = self.conn.cursor()
        id = args[0]
        name = args[1]
        city = args[2]
        phone = args[3]

        cur.execute("UPDATE employ SET name = %s, city = %s, phone = %s WHERE id = %s",(name,city,phone,id))
        print "Record Updated in Table"
        self.conn.commit()


    def addcolumn(self, *args):
        cur = self.conn.cursor()
        col_name = args[0]

        cur.execute("ALTER TABLE employ ADD col_name VARCHAR(15);")
        self.conn.commit()
        print "Column is added"

    def deletecol(self, *args):
        cur = self.conn.cursor()
        del_col = args[0]

        cur.execute("ALTER TABLE employ DROP COLUMN del_col;")
        self.con.commit()
        print "Column is deleted"

    def list_table_mysql(self):
        self.conn = db_config.connection_mysql()
        cur = self.conn.cursor()
        cur.execute('SHOW TABLES')

        rows = cur.fetchall()
        print "list of table : "
        for row in rows:
            print row

    def list_table_sqlite():
        self.conn = db_config.connection_mysql()
        cur = self.conn.cursor()
        cur.execute('SHOW TABLES')

        rows = cur.fetchall()
        print "list of table : "
        for row in rows:
            print row

    def delete(self,*args):
        cur = self.conn.cursor()
        i = args[0]
        try:
            cur.execute("DELETE FROM employ WHERE Id = %s",(i,))
            print "Record deleted"
        except Exception as e:
            print "Record with the given id not found"

