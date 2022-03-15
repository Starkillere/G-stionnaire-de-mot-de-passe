#-*-  coding:utf-8 -*-
import sqlite3

import sqlite3

def creat_gestionnaire_table():
       con = sqlite3.connect('database.db')
       cursor = con.cursor()

       cursor.execute('''CREATE TABLE gestionnaire (
                         id INTEGER PRIMARY KEY,
                         platforme TEXT NOT NULL,
                         nom TEXT NOT NULL,
                         password TEXT NOT NULL,
                         mail TEXT NOT NULL  
                  );''')
       con.commit()
       con.close() 

def creat_user_table():
       con = sqlite3.connect('database.db')
       cursor = con.cursor()
       cursor.execute('''CREATE TABLE user (
                         id INTEGER PRIMARY KEY AUTOINCREMENT,
                         nom TEXT NOT NULL,
                         master_password TEXT NOT NULL,
                         master_key TEXT NOT NULL
                  );''')
       con.commit()
       con.close() 

creat_user_table()
creat_gestionnaire_table()