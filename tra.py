# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 21:50:41 2020

@author: Duke Young
"""


from selenium.common.exceptions import NoSuchElementException,StaleElementReferenceException,TimeoutException   
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import json



#//*[@id="content-container"]/home-page/section/div/games-list/div/gamelist/div/div[2]/sport-league-header/div/div[2]/span



options = webdriver.ChromeOptions()
options.add_argument("start-maximized")

#driver = webdriver.Chrome(executable_path='chromedriver.exe',options=options)
#wait = WebDriverWait(driver,50)

def edit_leaguename(z,value):
    d = ""
    it= 0
    z = z.split()
    
    for i in z:
        if it == 0:
            d = d + i
        elif it == 1:
            d = d + i
        elif it == 2:
            i = i.replace(",","")
            d = d + i
        else:
            i = i.replace(",","")
            d = d + "-" + i
        it = it + 1
    d = value + d
    return d
    
final_list1 = []

leagues = {"tennis":"https://www.eazibet.com.gh/en/tennis/"}
def finding_leagues():
    driver = webdriver.Chrome(executable_path='chromedriver.exe',options=options)
    wait = WebDriverWait(driver,50)
    for l, value in leagues.items():
        driver.get(value)
        length_players = []
    
        Leag = '//*[@id="filter-league"]/div/div/div/select'
        Leag_text = wait.until(EC.presence_of_element_located((By.XPATH,Leag)))
        Leag_text = Leag_text.get_attribute("innerText")
        print("Leag_text")
        Leag_text = Leag_text.split("\n")
        #print(Leag_text)
        index = Leag_text.index("-- All Leagues alphabetically --")
    
        i = 0
        while i <= index:
            Leag_text.pop(0)
            i = i + 1
        #print(Leag_text)
#https://www.eazibet.com.gh/en/tennis/tennis-atp-nur-sultan-kazakhstan  
        L = [edit_leaguename(elem.lower(),value) for elem in Leag_text]
#v = edit_leaguename(L)
        #print(L)
        #print("")
    
        for li in L:
            v = li.split("-")
            if v[-3] == "itf":
                v.pop(-3)
            final_list1.append("-".join(v))
        players_xpath = '//div[@class = "game__team last_team"]'
        players = wait.until(EC.presence_of_all_elements_located((By.XPATH,players_xpath)))
        length_of_players = len(players)
        length_players.append(length_of_players)
    driver.close()
    return final_list1,Leag_text,length_players


