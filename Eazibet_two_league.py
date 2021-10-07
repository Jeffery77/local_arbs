
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
import csv



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
final_list = []

def write_to_csv(y):
    filename = "sorted_eazibet_tennis.csv"
    with open(filename,'w') as csvfile:
    # creating a csv writer object
        csvwriter = csv.writer(csvfile)
        fields = ['Team1','Team2','odd1','odd2','league','date']
    
      # writing the fields
        csvwriter.writerow(fields)
    
     # writing the data rows
    
        csvwriter.writerows(y)
        print("csv File created")

def eazi_odds():
    fi = []
    f = []
    oddsf = []
  
    try:
        market_odds = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME,"market")))
    except TimeoutException:
        return oddsf
    for m in market_odds:
        try:
            i =(m.get_attribute("id")).split("-")
            fi.append(m.get_attribute("id"))
            f.append(i[1])
        except IndexError:
            return oddsf
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
            try:
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
            except IndexError:
                return oddsf
    return oddsf

final,Leag_text,length_players = tra.finding_leagues()
final_list = []
date_list = []
time_list = []

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
    #try:
       
        
    oddsfinal = eazi_odds()
    try:
        Leag_name = wait.until(EC.presence_of_element_located((By.CLASS_NAME,'sport-league-header__groupname')))
     
        #match_odds_final.append(oddsfinal)
#        for o in oddsfinal:
#            match_odds_final.append(o)
   
        date_list = []
        time_list = []
        team_list = []
        team1 = []
        team2 = []
        odds1 = []
        odds2 = []
        final =  []
        player_names = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME,'game__teams')))
        date = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME,'standings__time')))
    
        time = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME,'standings__starttime')))
    except TimeoutException:
        pass
    try:
        for p in player_names:
            team_list.append(p.text)
            
        for d in date:
            date_list.append(d.text)
            
        for t in time:
            time_list.append(t.text)
    except NameError:
        pass
    except StaleElementReferenceException:
        pass
    flag = False
    for o in oddsfinal:
        if '+' in o[0]:
            flag = True
    if(len(oddsfinal) != 0 and len(time_list) != 0 and len(date_list) !=0 and( (len(date_list) == len(time_list) and len(time_list) == len(oddsfinal) and len(oddsfinal) == len(team_list)) ) and flag==False):
        print('Odds:',oddsfinal)
        print("Date is:",date_list)
        print("Time is:",time_list)
        print(len(oddsfinal))
        print(len(time_list)) 
        print(len(time_list))
        print(len(team_list))
        print("Team:",team_list)
        print("League is:",Leag_name.text)
        
        for t in team_list:
    #print(t.split("\n"))
            team1.append(t.split("\n")[0])
            team2.append(t.split("\n")[1])
    
        for o in oddsfinal:
            odds1.append(o[0])
            odds2.append(o[1])
    
    for i,t1 in enumerate(team1):
        try:
            final = [time_list[i],team1[i],team2[i],odds1[i],odds2[i],Leag_name.text,date_list[i]]
            final_list.append(final)
        except StaleElementReferenceException:
            pass
    
    print("\n")    
   #         final_list.append(p.text)
    #    Final_league_list.append(len(player_names))
            
      
           
           # print("cat")
           # print("j : " + j)
       
    #except:
     #   pass
print(final_list)
write_to_csv(final_list)