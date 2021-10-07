# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 12:29:16 2020

@author: Duke Young
"""
import json
import mysql.connector

mydb = mysql.connector.connect(
        host="localhost",
        user = "root",
        database = "local_odds"
        )

mycursor = mydb.cursor()

league_tables = ['premierleague1','laliga1']

# For creating tables
for league_table in league_tables:
    mycursor.execute("CREATE TABLE " + league_table +" (Id VARCHAR(255) PRIMARY KEY NOT NULL, Event VARCHAR(255) NOT NULL, Date VARCHAR(255) NOT NULL,BP_HOME FLOAT,BP_DRAW FLOAT,BP_AWAY FLOAT,PB_HOME FLOAT,PB_DRAW FLOAT,PB_AWAY FLOAT)")

