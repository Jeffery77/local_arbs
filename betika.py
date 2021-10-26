# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 10:29:13 2021

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
driver.get('https://betika.com.gh/s/tennis')

team_names_xpath1 = '//span[@class="prebet-match__teams__home"]'

team_names_xpath2 = '//div[@class="prebet-match__teams"]'
league_class_name = 'pull-left'
team_names_list1= []

last_name = ''
flag = True
while flag:
    team_names = wait.until(EC.presence_of_all_elements_located((By.XPATH,team_names_xpath1)))
    team_names_list1 = []

    for t in team_names:
        team_names_list1.append(t.text)
    print("Teams:")
    print(team_names_list1)
    if last_name != team_names_list1[-1]:
        last_name = team_names_list1[-1]
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(3)
    else:
        upcoming_button_xpath = '//button[@class="button account__payments__submit button button__secondary matches__more no-bg"]'
        upcoming_button = wait.until(EC.presence_of_element_located((By.XPATH,upcoming_button_xpath)))
        driver.execute_script("arguments[0].click();",upcoming_button)
        time.sleep(10)
        team_names = wait.until(EC.presence_of_all_elements_located((By.XPATH,team_names_xpath2)))
        league = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME,league_class_name)))
        team_names_list1 = []
        leagues = []

        for t in team_names:
            team_names_list1.append(t.text)
        for l in league:
            leagues.append(l.text)
            
        flag = False
