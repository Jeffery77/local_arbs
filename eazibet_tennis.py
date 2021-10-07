# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 11:04:38 2021

@author: dell
"""


from selenium.common.exceptions import NoSuchElementException,StaleElementReferenceException,TimeoutException   
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import json
import csv
#import tra



options = webdriver.ChromeOptions()
options.add_argument("start-maximized")

driver = webdriver.Chrome(executable_path='chromedriver.exe',options=options)
wait = WebDriverWait(driver,20)
First_name = []
Last_name = []
League_r = []
odds_f = []
date_time_t = []
time_t = []
Final_L = []
date_and_time_list = []
filename = "eazibet_tennis.json"

def get_nolink(Lengt):
    k = 0
    i = 1
    while i < Lengt:
        v = '//*[@id="content-container"]/div/home-page/section/div/games-list/div/gamelist/div/div/div[{}]/game/div/market-list/div/div[1]/div[1]'.format(i)
        avail = wait.until(EC.presence_of_element_located((By.XPATH,v)))
       # print(v)
        i = i + 1
        if avail.text == "Click to show available odds":
            k = i
        
           
    return k
    
def write_to_csv(y):
    filename = "sorted_eazibet_tennnis.csv"
    with open(filename,'w') as csvfile:
    # creating a csv writer object
        csvwriter = csv.writer(csvfile)
        fields = ['Team1','Team2','odd1','odd2','date','league']
    
      # writing the fields
        csvwriter.writerow(fields)
    
     # writing the data rows
    
        csvwriter.writerows(y)
        print("csv File created")

def eazi_odds():
    odds = []
    market_xpath = '//div[@class="market-list__element"]'
    market = wait.until(EC.presence_of_all_elements_located((By.XPATH,market_xpath)))
#v = wait.until()
    for m in market:
        #print(m.text)
        odds.append(m.text)
    
    print(odds)
    real_odds = []
    temp_odds = []

    for num, i in enumerate(odds):
        temp_odds = []
        c = (odds[num].split())
        try:
            if c[0] == '1': 
                temp_odds.append(c[1])
                if c[2] == '2':
                    temp_odds.append(c[3])
                    real_odds.append(temp_odds)
        except IndexError:
            temp_odds.append('0')
            temp_odds.append('0')
            real_odds.append(temp_odds)
    return real_odds


with open(filename) as f:
    data = json.load(f)

#v = ['https://www.eazibet.com.gh/en/tennis/tennis-itf-men-bagneres-de-bigorre-qual-m-fra-11a','https://www.eazibet.com.gh/en/tennis/tennis-atp-us-open-new-york-usa']

for l, v in data.items():
    driver.get(v[0])

#for i in v:
#    driver.get(i)
#driver.get("https://www.eazibet.com.gh/en/tennis/tennis-atp-us-open-new-york-usa")

    first_player_names_xpath = '//div[@class="game__team game__team__tennis"]'
    last_player_names_xpath = '//div[@class="game__team last_team"]'
    League_xpath = '//span[@class="sport-league-header__groupname"]'
    odds_xpath = '//div[@class="odd-button__value"]'
    date_time_xpath = '//div[@class="standings__time"]'
    time_xpath = '//div[@class="standings__starttime"]'
    try:
        players = wait.until(EC.presence_of_all_elements_located((By.XPATH,first_player_names_xpath)))
        players1 = wait.until(EC.presence_of_all_elements_located((By.XPATH,last_player_names_xpath)))
        League = wait.until(EC.presence_of_element_located((By.XPATH,League_xpath)))
        odds = wait.until(EC.presence_of_all_elements_located((By.XPATH,odds_xpath)))
        date_time = wait.until(EC.presence_of_all_elements_located((By.XPATH,date_time_xpath)))
        time = wait.until(EC.presence_of_all_elements_located((By.XPATH,time_xpath)))
    except TimeoutException:
        continue
        
    First_name = []
    Last_name = []
    League_r = []
    odds_f = []
    date_time_t = []
    for p in players:
        # print(p.text)
        First_name.append(p.text)
        League_r.append(League.text)
    
    for p in players1:
    #print(p.text)
        Last_name.append(p.text)
    
    for d in date_time:
        date_time_t.append(d.text)
    odds_f = eazi_odds()
    
    for l in time:
        time_t.append(l.text)
    try:
        err =  get_nolink(len(First_name))
    except TimeoutException:
        continue
    if err != 0:
        First_name.pop(err - 2)
        Last_name.pop(err - 2)
        League_r.pop(err -  2)
        date_time.pop(err - 2)
        time.pop(err - 2)
    
   # print(First_name)
   # print(len(First_name))
   # print("\n")
   # print(Last_name)
   
   # print(len(Last_name))
   # print("\n")
   # print(League_r)
   # print(len(League_r))
   # print("\n")
   # print(odds_f)
   # print(len(odds_f))
   # print(err)
    print("Time t:",len(time_t))
    print("date:",len(date_time_t))
    for i, k in enumerate(time_t):
        try:
            v = date_time_t[i] + " " +  time_t[i]
            date_and_time_list.append(v)
        except IndexError:
            v = "NULL " + time_t[i] 
            date_and_time_list.append(v)
        
        
    
    for num,f in enumerate(First_name):
        try:
            L = [First_name[num],Last_name[num],odds_f[num][0],odds_f[num][1],date_and_time_list[num],League_r[num]]
            Final_L.append(L)
        except IndexError:
            continue
#print(First_name)
#print(len(First_name))
#print("\n")
#print(date_time_t)
#print(len(date_time_t))
#print("\n")
#print(time_t)
#print(len(time_t))
print(Final_L)
write_to_csv(Final_L)