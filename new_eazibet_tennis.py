# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 14:51:27 2021

@author: dell
"""


# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 18:02:54 2020

@author: Duke Young
"""

from selenium.common.exceptions import NoSuchElementException,StaleElementReferenceException,TimeoutException   
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import json
import tra



#//*[@id="content-container"]/home-page/section/div/games-list/div/gamelist/div/div[2]/sport-league-header/div/div[2]/span



options = webdriver.ChromeOptions()
options.add_argument("start-maximized")

driver = webdriver.Chrome(executable_path='chromedriver.exe',options=options)
wait = WebDriverWait(driver,20)
fi = []
f = []
oddsf = []
oddsfinal = []
match_odds_final = []
Final_league_list = []

def eazi_odds():
    fi = []
    f = []
    oddsf = []
    market_odds = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME,"market")))
    
    for m in market_odds:
        i =(m.get_attribute("id")).split("-")
        fi.append(m.get_attribute("id"))
        f.append(i[1])
    try:
        if f[0] == f[1]:
            for k in fi:
                odds1 = []
                market_odds = '//*[@id="{}"]/div[2]/div'.format(k)
                # print(market_odds)
                odds = wait.until(EC.presence_of_element_located((By.XPATH,market_odds)))
            
                odds = odds.get_attribute("innerText")
                odds_final = odds.split("\n")
           
                odds1.append(odds_final[1])
                odds1.append(odds_final[3])
                oddsf.append(odds1)
        else:
            print("Both columns present")
            for i in range(len(fi)):
                if i % 2 == 0:
                    odds1 = []
                    market_odds = '//*[@id="{}"]/div[2]/div'.format(fi[i])
                    #print(market_odds)
                    odds = wait.until(EC.presence_of_element_located((By.XPATH,market_odds)))
                    # print("odds")
                    odds = odds.get_attribute("innerText")
                    odds_final = odds.split("\n")
                    #print(odds_final[1])
                    #print(odds_final[3])
                    odds1.append(odds_final[1])
                    odds1.append(odds_final[3])
                    oddsf.append(odds1)
    except IndexError:
        for k in fi:
            print("Only one row available")
            odds1 = []
            market_odds = '//*[@id="{}"]/div[2]/div'.format(k)
            # print(market_odds)
            odds = wait.until(EC.presence_of_element_located((By.XPATH,market_odds)))
            
            odds = odds.get_attribute("innerText")
            odds_final = odds.split("\n")
           
            odds1.append(odds_final[1])
            odds1.append(odds_final[3])
            oddsf.append(odds1)
    return oddsf

final,Leag_text,length_players = tra.finding_leagues()
final_list = []
#leagues = ["https://www.eazibet.com.gh/en/tennis/tennis-itf-women-tyler-tx-doubles-w-usa-42a"]
print("final")
print(final)
#//*[@id="content-container"]/home-page/section/div/games-list/div/gamelist/div/div[2]
for value in final:
    if "win" in value:
        continue
    
    driver.get(value)
    if(driver.current_url == "https://www.eazibet.com.gh/en/tennis"):
        continue
    try:
       
        
        oddsfinal = eazi_odds()
        print(oddsfinal)
        #match_odds_final.append(oddsfinal)
        #for o in oddsfinal:
        #    match_odds_final.append(o)
        #player_names = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME,'game__teams')))
        #for p in player_names:
        #    final_list.append(p.text)
        #Final_league_list.append(len(player_names))
            
      
           
           # print("cat")
           # print("j : " + j)
       
    except:
        pass

print("League types:")
print(Leag_text)
print(len(Leag_text))
print("\n")
print(Final_league_list)
print(len(Final_league_list))
print()
u = {}

"""
for x in range(len(final_list)-1):
    #print(a[x] + b[x])
    u[x] = oddsfinal[x] + final_list[x]
    
print(u)
"""
print("odds final :")
print(match_odds_final)
print("length of odds")
print(len(match_odds_final))
print("final list:")
print(final_list)
print("length of final list")
print(len(final_list))
#print("final:")
#print(final)