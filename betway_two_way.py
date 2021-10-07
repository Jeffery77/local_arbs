# -*- coding: utf-8 -*-
"""
Created on Fri Sep 10 17:48:41 2021

@author: dell
"""
from selenium.common.exceptions import NoSuchElementException,StaleElementReferenceException,TimeoutException   
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import json
import time as y
import csv



def write_to_csv(y):
    filename = "sorted_betpawa_tennnis.csv"
    with open(filename,'w') as csvfile:
    # creating a csv writer object
        csvwriter = csv.writer(csvfile)
        fields = ['Name','Branch','Year','CGPA']
    
      # writing the fields
        csvwriter.writerow(fields)
    
     # writing the data rows
    
        csvwriter.writerows(y)
        print("csv File created")


options = webdriver.ChromeOptions()
options.add_argument("start-maximized")

driver = webdriver.Chrome(executable_path='chromedriver.exe',options=options)
wait = WebDriverWait(driver,20)


def tennis():
    league = ['https://www.betpawa.com.gh/']
    Leag_type_and_names = []
    odds_list = []
    datetime_list = []
    players = []
    time = []
    final_list = []
    names_list = []
    final_list_final = []
    
    for l in league:
        driver.get(l)
        
        category_selector_xpath = '//*[@id="view-wrapper"]/div[1]/div[1]/div/div/select'
        category_selector = wait.until(EC.presence_of_element_located((By.XPATH,category_selector_xpath)))
        category_selector.click()
        tennis_category_xpath = '//select/option[@value="452"]'
        tennis_category = wait.until(EC.presence_of_element_located((By.XPATH,tennis_category_xpath)))
        tennis_category.click()
        category_selector.click()
        
        y.sleep(5)
        time_xpath = '//div[@class="times"]'
        player_names_xpath = '//p[@class="title team"]'
        league_type_xpath = 'sub-title league'
        league_type = wait.until(EC.presence_of_all_elements_located((By.XPATH,'//p[@class="sub-title league"]')))
        player_names = wait.until(EC.presence_of_all_elements_located((By.XPATH,player_names_xpath)))
        times = wait.until(EC.presence_of_all_elements_located((By.XPATH,time_xpath)))
       
    for l in league_type:
        #print(l.text)
        Leag_type_and_names.append(l.text)
        
    players = [p.text for p in player_names]
    time = [t.text for t in times]
    
    odds_class_name = 'event-bets'
    odds = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME,odds_class_name)))
    
    for o in odds:
        #print(o.text)
        odds_list.append(o.text)
   
    for i,b in enumerate(Leag_type_and_names):
        n = odds_list[i].split("\n")
        odd1 = n[1]
        odd2 = n[3]
        list1 = [odd1,odd2,time[i],Leag_type_and_names[i]]
        final_list.append(list1)
         
    for i,b in enumerate(players):
       p = i + 1
       if p % 2 == 1:
           temp_array = [players[i],players[p]]
           names_list.append(temp_array)
    for i,b in enumerate(names_list):
        final = [names_list[i][0],names_list[i][1],final_list[i][0],final_list[i][1],final_list[i][2],final_list[i][3]]
        final_list_final.append(final)
        
    print(final_list_final)
    write_to_csv(final_list_final)
    
try:
    tennis()
except:
    tennis()