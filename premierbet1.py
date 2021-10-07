# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 11:03:31 2020

@authors: Duke Young, M. Chase
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


sports_league = {'premier-league':'https://www.premierbet.com.gh/#/sports/all/1047177/','la-liga':'https://www.premierbet.com.gh/#/sports/all/1047364/'}
container = []

sorted_league = {}
def sort_values(list,key):
    wanted = [0,1,2,3,4,5,6,7]
   
    lit1 = []
   
    for l in list:
        lit = []
   
        # Removing the first 0 in the list
        l.pop(0)
    
    
        #Getting the first 8 elements and appending it to a list
        for ele in sorted(wanted,reverse=True):
            y=(l.pop(ele))
                    
               
                
            lit.append(y)
        
        lit1.append(lit)
   
    
       
    sorted_league[key] = lit1
    
    
    return sorted_league

for key,value in sports_league.items():
    i = 1
    driver.get(value)
    container = []
    while True:
        try:
            match_string = '//*[@id="widget-Z1Q5O5C0O5U6M4Y9A3S7785"]/div/div/div[2]/div/div[2]/div[3]/div[2]/div[{}]'.format(i)
    
            matches = wait.until(EC.presence_of_element_located((By.XPATH,match_string)))
            matches = matches.get_attribute("innerText")
            final_matches = matches.split("\n")
            #print(final_matches)
            container.append(final_matches)
            
            i = i + 1
        except TimeoutException:
            break
    container1 = copy.deepcopy(container)
    sorted_league =sort_values(container1,key)
 
print(sorted_league)
print("Done")

   
def convert_data(data_dictionary):
    filename = 'premierbet_data.json'
    with open(filename, "w") as f:
        json.dump(sorted_league, f, indent=4)

    f.close()
    
convert_data(sorted_league)

driver.close()

def add_unique_keys(json_data):
    # open scraped data in read mode
    with open(json_data, 'r') as file:
        scraped_data = json.load(file)

    # set counter for looping through scraped data
    # create new dictionary[dict-1] to contain id-ed scraped data 
    counter = 0
    data_dict = {}

    scraped_data_length = len(scraped_data)

    # while loop for scraped data
    while counter < scraped_data_length:
        
        for league, event_list in scraped_data.items():

            for event in event_list:
            
            #event_dict = {}

                
                home_team = event[3]
                home_team_break_points = home_team.split()
                home_team_key = max(home_team_break_points, key=len)
                home_team_ID = home_team_key[0] + home_team_key[1]

                away_team = event[5]
                away_team_break_points = away_team.split()
                away_team_key = max(away_team_break_points, key=len)
                away_team_ID = away_team_key[0] + away_team_key[1]

                event_date = event[6]      
                event_date_ID = event_date[0] + event_date[1]

                special_string = event_date_ID + home_team_ID.title() + away_team_ID.title()

                if league == "premier-league":
                    special_string += 'epl'
                elif league == "la-liga":
                    special_string += 'spl'

                print(special_string)

                data_dict[special_string] = event

                #data_dict.append(event_dict)

      
        counter += 1
    print(data_dict)

    sorted_data = 'premierbet_data.json'
    with open(sorted_data, "w") as f:
        json.dump(data_dict, f, indent=4)
    f.close()

add_unique_keys('premierbet_data.json')