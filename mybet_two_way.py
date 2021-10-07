# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 23:37:38 2020

@author: Duke Young
"""

from selenium.common.exceptions import NoSuchElementException,StaleElementReferenceException,TimeoutException   
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import json



options = webdriver.ChromeOptions()
options.add_argument("start-maximized")

driver = webdriver.Chrome(executable_path='chromedriver.exe',options=options)
wait = WebDriverWait(driver,20)


url_code = ""
league_name = []
datetime_list = []
event_info_list_section = []
event_info_list_total = []

filename = "mybet.json"

with open(filename) as f:
    data = json.load(f)

for l,value in data.items():
    url_code = url_code + "-" + value
    
url_code = url_code[1:]

print(url_code)

url = "https://www.mybet.africa/sport/odds?tournaments={}&timeFrame=all".format(url_code)

driver.get(url)

flag1 =True
counter = 1

while flag1:
    try:
        league_xpath = '//*[@id="nvsOddsPage"]/div/div[{}]/div[1]/div[2]/h1/span'.format(counter)
        league_type = wait.until(EC.presence_of_element_located((By.XPATH,league_xpath)))
        league_name.append(league_type.text)
        datetime_xpath = '//*[@id="nvsOddsPage"]/div/div[{}]/div[4]/div/nvs-odds-table/div/div[2]/div[1]/div[1]/h3/nvs-configure-date-time-for-view'.format(counter)
        datetime = wait.until(EC.presence_of_element_located((By.XPATH,datetime_xpath)))
        datetime_list.append(datetime.text)
        event_info_xpath ='//*[@id="nvsOddsPage"]/div/div[{}]/div[4]/div/nvs-odds-table/div/div[2]/div[3]'.format(counter)
        event_info = wait.until(EC.presence_of_element_located((By.XPATH,event_info_xpath)))
        event_info_list_section = (event_info.text).split("\n")
        event_info_list_total.append(event_info_list_section)
        counter = counter + 1
    except TimeoutException:
        break




print(event_info_list_total)
print(league_name)
print(datetime_list)

