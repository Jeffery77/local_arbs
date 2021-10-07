# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 16:40:57 2020

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

league_table = 'PremierLeague'
leag = ""
def league_t(key):
    global leag
    if "la-liga" in key:
        leag = "laliga"
    if "English-premier-league" in key:
        leag = "premierleague"

filename = "betplanet_data.json"
filename1 = "premierbet_data.json"

def threeway_betplanet(filename):
    
    league = []
    val = []



    with open(filename) as f:
        data = json.load(f)
    
    for key,value in data.items():
        z =key.split()
        u = z[0] + " " + z[1] + " " +  z[2]
        print(u)
        league_t(key)
    
        for key1,value1 in value.items():
            spec=key1
            Event = value1[5] + " vs " + value1[1]
            Date = u + " " + value1[6] 
            BP_HOME = value1[4]
            BP_DRAW = value1[2]
            BP_AWAY = value1[0]
            print(key1)
            print(value1)
            sql = "INSERT INTO " + leag + " (Id,Event,Date,BP_HOME,BP_DRAW,BP_AWAY) VALUES (%s,%s,%s,%s,%s,%s)"
            val = (spec,Event,Date,BP_HOME,BP_DRAW,BP_AWAY)
            mycursor.execute(sql,val)
            mydb.commit()
            
        print("\n")
    

#threeway_betplanet(filename)

##leag = """premierleague"""

##sql = """UPDATE """ + leag +""" set PB_HOME= %s WHERE Id = %s """
##val = ("7","17ArMaepl" )
##mycursor.execute(sql,val)
##mydb.commit()


def threeway_premierbet(filename1):
    with open(filename1) as f:
        data = json.load(f)

    for key,value in data.items():
        spec = key
        Event = value[5] + " " + value[4] + " " + value[3]
        PB_HOME = value[2]
        PB_DRAW = value[1]
        PB_AWAY = value[0]
    
        if "epl" in spec:
            leag = "premierleague"
        if "spl" in spec:
            leag = "laliga"
        
    
        sql = """UPDATE """ + leag +""" set PB_HOME= %s WHERE Id = %s """
        val = (PB_HOME,spec )
        mycursor.execute(sql,val)
        sql = """UPDATE """ + leag +""" set PB_DRAW= %s WHERE Id = %s """
        val = (PB_DRAW,spec )
        mycursor.execute(sql,val)
        sql = """UPDATE """ + leag +""" set PB_AWAY= %s WHERE Id = %s """
        val = (PB_AWAY,spec )
        mycursor.execute(sql,val)
        mydb.commit()
        print(PB_DRAW)
    
  
   
    
#print(data)
threeway_betplanet(filename1)
mycursor.close()
