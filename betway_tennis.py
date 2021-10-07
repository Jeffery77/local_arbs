# -*- coding: utf-8 -*-
"""
Created on Fri Sep 10 20:53:12 2021

@author: dell
"""

from selenium.common.exceptions import NoSuchElementException,StaleElementReferenceException,TimeoutException   
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import json
import csv
import time

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")

driver = webdriver.Chrome(executable_path='chromedriver.exe',options=options)
wait = WebDriverWait(driver,20)
date_league_list = []
team_list = []
odds_list = []
date_list = []
odds1 = []
odds2 = []
team2 = []
team1 = []
league_list = []

final_list = []
def write_to_csv(y):
    filename = "sorted_betway_tennnis.csv"
    with open(filename,'w') as csvfile:
    # creating a csv writer object
        csvwriter = csv.writer(csvfile)
        fields = ['Team1','Team2','odd1','odd2','date','league']
    
      # writing the fields
        csvwriter.writerow(fields)
    
     # writing the data rows
    
        csvwriter.writerows(y)
        print("csv File created")
def separate_date_league(date_league):
    date_final= []
    league_final= []
    for d in date_league:
       # print(d)
        date_temp = []
        ll = d.split(" ")
        print("\n")
        #print(ll)
        try:
            date_temp.append(ll.pop(0))
            date_temp.append(ll.pop(0))
            date_temp.append(ll.pop(0))
        except IndexError:
            continue
        yy = ' '.join(date_temp)
        date_temp = [yy]
        #print(date_temp)
        date_final.append(date_temp)
        zz = ' '.join(ll)
        league = [zz]
        league_final.append(league)
     #   print(zz)
     
        
        
   # print(date_final)
    #print(len(date_final))
    #print("\n")
    #print(league_final)
    #print(len(league_final))
    return date_final,league_final


driver.get('https://www.betway.com.gh/sport/tennis')
upcoming = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="tab_UC"]/span[2]')))
driver.execute_script("arguments[0].click();", upcoming)
flag = True

while flag:
    try:
        load_more_xpath = '//button[@id="loadMoreButton"]'
        load_more = wait.until(EC.presence_of_element_located((By.XPATH,load_more_xpath)))
        driver.execute_script("arguments[0].click()",load_more)
        time.sleep(4)
        if load_more.text != 'Load more...':
            print("load more not available")
            break
    except:
        flag = False
        print("load more not available")

date_xpath = '//label[@class="ellips theOtherFont  label__league_title"]'
date = wait.until(EC.presence_of_all_elements_located((By.XPATH,date_xpath)))
team_xpath = '//div[@class="outcome-title text-left  "]'
team = wait.until(EC.presence_of_all_elements_located((By.XPATH,team_xpath)))
odds_xpath = '//div[@class="outcome-pricedecimal "]'
odds = wait.until(EC.presence_of_all_elements_located((By.XPATH,odds_xpath)))


    
for d in date:
    print(d.text)
    date_league_list.append(d.text)
    
for t in team:
    team_list.append(t.text)
    
for o in odds:
    odds_list.append(o.text)
date_list,league_list = separate_date_league(date_league_list) 
for i,o in enumerate(odds_list):
    v = i + 1
    if v % 2 == 0:
        odds2.append(o)
    else:
        odds1.append(o)
        
for i,t in enumerate(team_list):
    v = i + 1
    if v % 2 == 0:
        team2.append(t)
    else:
        team1.append(t)
print("team1:",len(team1))
print("team2:",len(team2))
print("odds1:",len(odds1))  
print("odds2:",len(odds2))  
print("date:",len(date_list))
print("League list:",len(league_list))
for i, t in enumerate(team1):
    temp_list = []
    if odds[i] == '':
        continue
    temp_list =[team1[i],team2[i],odds1[i],odds2[i],date_list[i][0],league_list[i][0]]
    final_list.append(temp_list)

print("\n")    
print(final_list)
write_to_csv(final_list)

# preprocessing and send dat