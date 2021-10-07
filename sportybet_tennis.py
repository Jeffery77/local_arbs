# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 15:01:35 2021

@author: dell
"""

from selenium.common.exceptions import NoSuchElementException,StaleElementReferenceException,TimeoutException   
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import json
import copy




options = webdriver.ChromeOptions()
options.add_argument("start-maximized")

driver = webdriver.Chrome(executable_path='chromedriver.exe',options=options)
wait = WebDriverWait(driver,10)
lists = []
league_list = []

filename = 'sportybet_tennis.json'

with open(filename) as f:
    data = json.load(f)
    
 
for l, v in data.items():
    driver.get(v[0])

    info_path= '//div[@class="m-table-row m-content-row match-row"]'
    count = 1
    #info = driver.find_elements_by_xpath(info_path)
    try:
        info = wait.until(EC.presence_of_all_elements_located((By.XPATH,info_path)))
    except TimeoutException:
        continue
        
    for i in info:
        lists = i.text.split("\n")
        lists.append(l)
        lists.pop(1)
        lists.pop(5)
        lists.pop(5)
        lists.pop(5)
        lists.pop(5)
        print(lists)
        league_list.append(lists)
print(league_list)
 
