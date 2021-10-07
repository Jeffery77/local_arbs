# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 08:59:14 2021

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



driver.get('https://www.eazibet.com.gh/en/tennis')

League_button_xpath = '//*[@id="filter-league"]/div/div/div/select'
League_button = wait.until(EC.visibility_of((By.XPATH,League_button_xpath)))


driver.
driver.execute_script("arguments[0].click();", League_button)