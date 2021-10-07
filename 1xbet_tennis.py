# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 11:21:55 2021

@author: dell
"""


from selenium.common.exceptions import NoSuchElementException,StaleElementReferenceException,TimeoutException   
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import json
import time 



options = webdriver.ChromeOptions()
options.add_argument("start-maximized")

driver = webdriver.Chrome(executable_path='chromedriver.exe',options=options)
wait = WebDriverWait(driver,10)
wait2 = WebDriverWait(driver,5)
lists = []

def convert_to_time(li):
    result = time.localtime()
    if len(li) == 3:
        d = int(li[0])
        h = int(li[1])
        m = int(li[2])
        day = result.tm_mday + d
        hour = result.tm_hour + h
        minute = result.tm_min+ m
        if minute % 5 != 0:
            minute = minute + 1
    
        if minute >= 60:
            minute = minute % 60
            hour = hour + 1
        
        if hour >= 24:
            hour = hour % 24
            day = day + 1
      
            
    if len(li) == 1:
         m = int(li[0])
         minute = result.tm_min+ m
         hour = result.tm_hour
         day = result.tm_mday
         if minute % 5 != 0:
             minute = minute + 1
         if minute >= 60:
            minute = minute % 60
            hour = hour + 1
            
    if  len(li) == 2:
        h = int(li[0])
        m = int(li[1])
        hour = result.tm_hour + h
        minute  = result.tm_min+ m
        if minute % 5 != 0:
            minute = minute + 1
        day = result.tm_mday
        if minute >= 60:
            minute = minute % 60
            hour = hour + 1
        if hour >= 24:
            hour = hour % 24
            day = day + 1
            
        
        
    m  = result.tm_mon
    tii = str(day) + " " + str(m) + " " + str(hour) +":"+ str(minute)
        
  
    #print(119 % 60)
    
    tim = [tii]
    return tim
name_list = []
odds_list = []
filename = '1xbet_tennis.json'

with open(filename) as f:
    data = json.load(f)
ff = ['https://1xbet.com.gh/live/Tennis/1176821-Challenger-Barletta/']
for l in ff:
    
    driver.get(l)
    
    players_info_path = '//div[@class="c-events__item c-events__item_game"]'
    Team_info_path = '//span[@class="c-events__teams"]'
    date_info_path = '//div[@class="c-events__time min"]'
    league_info_xpath = '//*[@id="games_content"]/div/div[2]/div/div/div[1]/div/div[2]/a'
    players_info = driver.find_elements_by_xpath(players_info_path)
    team_info = driver.find_elements_by_xpath(Team_info_path)
    #team = wait.until(EC.presence_of_all_elements_located((By.XPATH,team_info)))
    #date_css = 'games_content > div > div:nth-child(2) > div > div > div:nth-child(2) > div.c-events__item.c-events__item_game > div.c-events__time-info > div > span''
    try:
        league_info = wait.until(EC.presence_of_element_located((By.XPATH,league_info_xpath)))
    except TimeoutException:
        continue
    try:
        date_info = wait.until(EC.presence_of_all_elements_located((By.XPATH,date_info_path)))
    except:
        pass
    #all_info_xpath ='//div[@class="c-events__item c-events__item_game"]'
    
    #all_info = wait.until(EC.presence_of_all_elements_located((By.XPATH,all_info_xpath)))
    print("League name:",league_info.text)
    #for x in all_info:
    #    print(x.span)
    for p in players_info:
        #print(p.text)
        #print("\n")
        lists = p.text.split("\n")
     #   lists.append(l)
        #print(lists)
        odds_list.append(lists)
    
        
    for t in team_info:
        print(t.get_attribute('title'))
        print("\n")
        name_list.append(t.get_attribute('title'))
    #first_date_info_xpath = "//p/span"
    #first_date = wait.until(EC.presence_of_all_elements_located(((By.XPATH,first_date_info_xpath))))
    time_list = []
    
    for f in date_info:
        time_list_temp = []
        te = f.get_attribute('title')
        t = te.split(" ")
        if(len(t) == 9):
            d = t[3]
            h = t[5]
            m = t[7]
            time_list_temp = [d,h,m]
            #print("Day:",d)
            #print("hour:",h)
            #print("minute;",m)
            #print(time_list_temp)
            lll = convert_to_time(time_list_temp)
            print(lll)
            time_list.append(lll)
            lll = []
        if(len(t) == 7):
            h = t[3]
            m = t[5]
            time_list_temp = [h,m]
            #print("hour:",h)
            #print("minute:",m)
            #print(time_list_temp)
            lll = convert_to_time(time_list_temp)
            print(lll)
            time_list.append(lll)
            lll = []
        if(len(t) == 5):
            m = t[3]
            time_list_temp = [m]
            #print("minute:",m)
            #print(time_list_temp)
            lll = convert_to_time(time_list_temp)
            print(lll)
            time_list.append(lll)
            lll = []
        #print("t",t)
        #print("\n")
        #print(time_list)
        #print("\n")
        #print(name_list)
        #print("\n")
        #print(odds_list)
        
for i,k in enumerate(name_list):
    li = []
    try:
        li = [time_list[i][0],k,odds_list[i][1],odds_list[i][3]]
    except:
        continue
    print("\n")
    print(li)
    #print(t)
    

#for d in date_info:
#    print(d.text)
    
#//*[@id="games_content"]/div/div[2]/div/div/div[2]/div[2]/div[2]/div/span
#//*[@id="games_content"]/div/div[2]/div/div/div[4]/div/div[2]/div/span
#//*[@id="games_content"]/div/div[2]/div/div/div[3]/div/div[2]/div/span
#//*[@id="games_content"]/div/div[2]/div/div/div[4]/div/div[2]/div/span


#//*[@id="games_content"]/div/div[2]/div/div/div[2]/div[2]/div[2]/div/span

#//*[@id="games_content"]/div/div[2]/div/div/div[3]/div/div[2]/div/span
#//*[@id="games_content"]/div/div[2]/div/div/div[11]/div/div[2]/div/span
#//*[@id="games_content"]/div/div[2]/div/div/div[12]/div/div[2]/div/span



