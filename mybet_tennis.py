# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 21:09:20 2021

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

def write_to_csv(y):
    filename = "sorted_mybet_tennis.csv"
    with open(filename,'w') as csvfile:
    # creating a csv writer object
        csvwriter = csv.writer(csvfile)
        fields = ['Team1','Team2','odd1','odd2','date','league']
    
      # writing the fields
        csvwriter.writerow(fields)
    
     # writing the data rows
    
        csvwriter.writerows(y)
        print("csv File created")
        
def sort_info(num,g,date,league):
    gt = (g[num].split("\n"))

    count = 0
    team_info = []
    large_team_info = []
    for i, t in enumerate(gt):
        #print(i)
    
        if ":" in t and i != 0:
            #print(team_info)
            team = team_info[1].split("-")
            da = team_info[0] + " " + date
            team_info_a = [team[0],team[1],team_info[2],team_info[3],da,league]
            large_team_info.append(team_info_a)
            team_info = []
        team_info.append(t)
    team = team_info[1].split("-")
    da = team_info[0] + " " + date
    team_info_a = [team[0],team[1],team_info[2],team_info[3],da,league]
    large_team_info.append(team_info_a)
    for l in large_team_info:
        final_list.append(l)
    print(large_team_info)

def get_info():
    tournament_xpath = '//*[@id="nvsOddsPage"]/div/div/div[1]/div[2]/h1/span'
                 
    Date_xpath = '//*[@id="nvsOddsPage"]/div/div[1]/div[4]/div/nvs-odds-table/div/div[2]/div[1]/div[1]/h3/nvs-configure-date-time-for-view'
    team_names_xpath = '//div[@class="content--inner"]'
    
    Date_xpath_1 = '//*[@id="nvsOddsPage"]/div/div/div[4]/div/nvs-odds-table/div/div[2]/div[1]/div[1]/h3/nvs-configure-date-time-for-view'
    Date_xpath_2 = ' //*[@id="nvsOddsPage"]/div/div/div[4]/div/nvs-odds-table/div/div[3]/div[1]/div[1]/h3/nvs-configure-date-time-for-view'
    team_list = []
    tournament_header = wait.until(EC.presence_of_element_located((By.XPATH,tournament_xpath)))
    Date = wait.until(EC.presence_of_element_located((By.XPATH,Date_xpath_1)))
    team_names = wait.until(EC.presence_of_all_elements_located((By.XPATH,team_names_xpath)))
    for t in team_names:
        team_list.append(t.text)
        #print(t.text)
    print(tournament_header.text)
    print(Date.text)
    #print(team_list)
    sort_info(0,team_list,Date.text,tournament_header.text)
    print
    try:
        Date_2 = wait2.until(EC.presence_of_element_located((By.XPATH,Date_xpath_2)))
        print(Date_2.text)
        sort_info(1,team_list,Date.text,tournament_header.text)
    except TimeoutException:
        pass
        

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")

driver = webdriver.Chrome(executable_path='chromedriver.exe',options=options)
wait = WebDriverWait(driver,20)
wait2 = WebDriverWait(driver,5)
Date_list = []
final_list = []

driver.get('https://www.mybet.africa/sport/odds?timeFrame=all')
# Change the locator when the tennis tab has been shifted
tennis_locator_number = 4

  #                 //*[@id="nvs-left-sidebar"]/div/div[5]/nvs-widget-list-manager/div/div[2]/div[4]/div[1]
tennis_tab_xpath = '//*[@id="nvs-left-sidebar"]/div/div[5]/nvs-widget-list-manager/div/div[2]/div[{}]/div[1]/span[2]'
tennis_tab_xpath = tennis_tab_xpath.format(tennis_locator_number)
tennis_tab = wait.until(EC.presence_of_element_located((By.XPATH,tennis_tab_xpath)))

driver.execute_script("arguments[0].click();", tennis_tab)

for v in range(15):
    flag = True
    if v == 0:
        continue
   
    tournament_dropdown_xpath = '//*[@id="nvs-left-sidebar"]/div/div[5]/nvs-widget-list-manager/div/div[2]/div[4]/div[2]/div[{}]/div[1]/div[3]/i'

    #icon_select_xpath = icon_select_xpath.format(v)
    tournament_dropdown_xpath = tournament_dropdown_xpath.format(v)
    try:
        #icon_select = wait.until(EC.presence_of_element_located((By.XPATH,icon_select_xpath)))
        tournament_dropdown = wait.until(EC.presence_of_element_located((By.XPATH,tournament_dropdown_xpath)))
        driver.execute_script("arguments[0].click();",tournament_dropdown)
    except TimeoutException:
        break
    p = 1
    while flag:
        try:
       
            icon_select_xpath = '//*[@id="nvs-left-sidebar"]/div/div[5]/nvs-widget-list-manager/div/div[2]/div[{}]/div[2]/div[{}]/div[2]/label[{}]/span[1]'
            icon_select_xpath = icon_select_xpath.format(tennis_locator_number,v,p)
            #.000021415869++-print(icon_select_xpath)
            icon_select = wait.until(EC.presence_of_element_located((By.XPATH,icon_select_xpath)))
            time.sleep(2)
            driver.execute_script("arguments[0].click();",icon_select)
            get_info()
            driver.execute_script("arguments[0].click();",icon_select)
            p = p + 1
       #     driver.execute_script("arguements[0].click()",icon)
        except TimeoutException:
            flag = False
            
    #get_info()
    print("next league title")
#print("Final list:")
#print(final_list)  
write_to_csv(final_list)
    #driver.execute_script("arguments[0].click();",tournament_dropdown)



