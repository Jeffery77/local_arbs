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


def get_info():
    tournament_xpath = '//h1[@class="tournament-header--title"]'
    Date_xpath = '//*[@id="nvsOddsPage"]/div/div[1]/div[4]/div/nvs-odds-table/div/div[2]/div[1]/div[1]/h3/nvs-configure-date-time-for-view'
    Date_xpath_format = '//*[@id="nvsOddsPage"]/div/div[{}]/div[4]/div/nvs-odds-table/div/div[{}]/div[1]/div[1]/h3/nvs-configure-date-time-for-view'

    tournament_header = wait.until(EC.presence_of_all_elements_located((By.XPATH,tournament_xpath)))
    Date = wait.until(EC.presence_of_element_located((By.XPATH,Date_xpath)))
    length = len(tournament_header)

    for i in range(length):
        if i == 0:
            continue
        Date_xpath_format = Date_xpath_format.format(i,2)
        try:
            Date = wait.until(EC.presence_of_element_located((By.XPATH,Date_xpath_format)))
            Date_list.append(Date.text)
        except TimeoutException:
            pass
    
    for t in tournament_header:
        print(t.text)


        print(Date_list)

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")

driver = webdriver.Chrome(executable_path='chromedriver.exe',options=options)
wait = WebDriverWait(driver,20)
Date_list = []

driver.get('https://www.mybet.africa/sport/odds?timeFrame=all')

tennis_tab_xpath = '//*[@id="nvs-left-sidebar"]/div/div[5]/nvs-widget-list-manager/div/div[2]/div[4]/div[1]/span[2]'
tennis_tab = wait.until(EC.presence_of_element_located((By.XPATH,tennis_tab_xpath)))
icon_select_xpath = '//*[@id="nvs-left-sidebar"]/div/div[5]/nvs-widget-list-manager/div/div[2]/div[4]/div[2]/div[1]/div[1]/div[2]/label/span'

driver.execute_script("arguments[0].click();", tennis_tab)
icon_select = wait.until(EC.presence_of_element_located((By.XPATH,icon_select_xpath)))

driver.execute_script("arguments[0].click();",icon_select)
get_info()




