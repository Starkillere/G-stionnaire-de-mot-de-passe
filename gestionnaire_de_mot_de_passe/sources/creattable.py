#-*-  coding:utf-8 -*-
import sqlite3

con = sqlite3.connect('database.db')
cursor = con.cursor()

cursor.execute('''CREATE TABLE gestionnaire (
                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                  platforme TEXT NOT NULL,
                  nom TEXT NOT NULL,
                  password TEXT NOT NULL,
                  mail TEXT NOT NULL  
           );''')
con.commit()
con.close()          
