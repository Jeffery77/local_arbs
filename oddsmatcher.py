# -*- coding: utf-8 -*-
"""
Created on Sun Oct 24 19:53:25 2021

@author: MILLICENT
"""


import pandas as pd

df_eazi = pd.read_csv('sorted_eazibet_tennis.csv')
df_betway = pd.read_csv('sorted_betway_tennnis.csv')
df_betpawa = pd.read_csv('sorted_betpawa_tennnis.csv')
# shows the number of columns you want to display
pd.set_option("display.max_columns",6)
# self explanatory gives info about the dataframe
#print(df.info())
#print(df)


print(df_eazi.head())
#print(df_eazi['league'])
# or use this
#print(df_eazi.league)
#print(df_eazi[['league','Team1','Team2']])
print("**************************")
#print(df_betway[['league','Team1','Team2']])
print("**************************")
#print(df_betpawa[['league','Team1','Team2']])

#print(df_betway.head())

