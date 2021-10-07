# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 14:10:00 2020

@author: Duke Young
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
wait = WebDriverWait(driver,20)


leagues = {}


sorted_league = {}
def sort_values(list,key):
    wanted = [0,1,2,3,4,5,6]
    
    lit1 = []
    for l in list:
        lit =[]
        
         # Removing the first 0 in the list
       # l.pop(0)
        
        #Getting the first 7 elements and appending it to a list
        for ele in sorted(wanted,reverse=True):
            y=(l.pop(ele))
            
            lit.append(y)
        lit1.append(lit)
    sorted_league[key] = lit1
    return sorted_league
  

filename = 'two_way_league_premierbet.json'
dd ={"US Open Men Singles":['https://www.premierbet.com.gh/#/sports/all/1046985/']}
with open(filename) as f:
    data = json.load(f)

    

for l,value in data.items():
    i = 1
    driver.get(value[0])
#for l,value in dd.items():
  #  i = 1
 #   driver.get(value[0])
    container = []
    while True:
        try:
            
            match_string = '//*[@id="widget-Z1Q5O5C0O5U6M4Y9A3S7785"]/div/div/div[2]/div/div[2]/div[3]/div[2]/div[{}]'.format(i)
    
            matches = wait.until(EC.presence_of_element_located((By.XPATH,match_string)))
            matches = matches.get_attribute("innerText")
            final_matches = matches.split("\n")
            #print("Final_matches")
            #print(final_matches)
            
            container.append(final_matches)
            
            i = i + 1
        except TimeoutException:
            break
    container1 = copy.deepcopy(container)
    sorted_league =sort_values(container1,l)
    print(sorted_league)