# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 09:28:36 2017

@author: River
"""
#%%
import sqlite3
connection=sqlite3.connect('test.sqlite')
cursor=connection.cursor()
cursor.execute("""SELECT DATE('NOW')""")
connection.commit()
connection.close()

#%%
connection=sqlite3.connect('coachdata.sqlite')
cursor=connection.cursor()
cursor.execute("""CREATE TABLE athletes(
                  id INTEGER RPIMARY KEY AUTO INCREMENT UNIQUE NOT NULL,
                  name TEXT NOT NULL,
                  dob DATE NOT NULL)""")
cursor.execute("""CREATE TABLE timing_data(
                athlete_id INTEGER NOT NULL,
                value TEXT NOT NULL,
                FOREIGN KEY(athlete_id) REFERENCES athletes)""")
connection.commit()
connection.close()

#%%
connection=sqlite3.connect('coachdata.sqlite')
cursor=connection.cursor()
name='Johnny Joe';dob="2011-2-2"
cursor.execute("""INSERT INTO athletes (name,dob) VALUES (?,?)""", (name,dob))
connection.commit()
cursor.execute("""SELECT id FROM athletes
              WHERE name=? AND dob=?""",(name,dob))
the_current_id=cursor.fetchone()[0]
connection.commit()
connection.close()
