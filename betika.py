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


options = webdriver.ChromeOptions()
options.add_argument("start-maximized")

driver = webdriver.Chrome(executable_path='chromedriver.exe',options=options)


wait = WebDriverWait(driver,20)
driver.get('https://betika.com.gh/s/tennis')
upcoming_xpath = '/html/body/div[3]/main/div[1]/div/div[2]/div/div[2]/button'
upcoming_xpath1 = '//button[@class="button account__payments__submit button button__secondary matches__more no-bg"]'

#load_matches = "/html/body/div[3]/main/div[1]/div/div[2]/div/div[2]/button"


upcoming_button = wait.until(EC.presence_of_element_located((By.XPATH,upcoming_xpath1)))

driver.execute_script("arguments[0].click();",upcoming_button)
driver.execute_script("arguments[0].click();",upcoming_button)
tournament_xpath = '//div[@class="pull-left"]'

tournaments = wait.until(EC.presence_of_all_elements_located((By.XPATH,tournament_xpath)))
for t in tournaments:
    print(t.text)