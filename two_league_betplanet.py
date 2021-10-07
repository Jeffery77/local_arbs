# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 19:05:34 2020

@authors: Duke Young, M.Chase
"""


from selenium.common.exceptions import NoSuchElementException,StaleElementReferenceException,TimeoutException   
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import copy
import json

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")

driver = webdriver.Chrome(executable_path='chromedriver.exe',options=options)
wait = WebDriverWait(driver,20)

sorted_dict = {}
def sort_tennis_league(list,key):
    start = 0
    length_of_list = len(list) - 1
    
    while(start < length_of_list):
         flag = True
        
         first_date = list.pop(0)

        
         day = first_date.pop(0)
         month = first_date.pop(0)
         #print(day)
         
         if day == "OUTRIGHT":
            start = start + 1
            continue
      
         if day == "IN-PLAY":
             start = start + 1
             continue
         
         first_date_date = day + " "  + month
         #print(first_date_date)
         #print(first_date)
         
         
         # Rmoving winner from the list
         first_date.pop(0)
         
         #Getting the first 5 elements
         wanted = 0,1,2,3,4
         
         z1 = []
         li = []
         while flag:
             
             try:
                 for ele in sorted(wanted,reverse=True):
                     y=(first_date.pop(ele))
                    
                     li.append(y)
                 
                 first_date.pop(0)
                 z1.append(li)
                 li = []
                 #print(li)
                 
             except IndexError:
                 flag = False
         start = start + 1
         if z1 in sorted_dict.values():
             pass
         else:
             sorted_dict[first_date_date + key] = z1
     

tennis_league_types = {'French-open-men-singles':['https://sports.betplanet.com.gh/home/wrapper/events?list=%5B%7B%22sport%22:5,%22leagues%22:%5B3886%5D%7D%5D','3886'],'French-open-men-doubles':['https://sports.betplanet.com.gh/home/wrapper/events?list=%5B%7B%22sport%22:5,%22leagues%22:%5B9331%5D%7D%5D','9331'],'ATP-COLOGNE-DOUBLES':['https://sports.betplanet.com.gh/home/wrapper/events?list=%5B%7B%22sport%22:5,%22leagues%22:%5B9961%5D%7D%5D','9961'],'ATP-SARDINIA_DOUBLES':['https://sports.betplanet.com.gh/home/wrapper/events?list=%5B%7B%22sport%22:5,%22leagues%22:%5B9962%5D%7D%5D','9962'],'ATP-ST.PETERSBURRB':['https://sports.betplanet.com.gh/home/wrapper/events?list=%5B%7B%22sport%22:5,%22leagues%22:%5B9958%5D%7D%5D','9958']}

filename = 'tennis_league.json'
with open(filename) as f:
    data = json.load(f)
    
#print(data)
container = []
container1 = []

for key,value in data.items():
    driver.get(value[0])
    i = 1
    while True:
        
        try:
    
            match_string = '//*[@id="{}"]/div/div[{}]'.format(value[1],i)
            matches = wait.until(EC.presence_of_element_located((By.XPATH,match_string)))
    
            matches = matches.get_attribute('innerText')
            final_matches = matches.split('\n')
            container.append(final_matches)
            #print(matches)
            i = i + 1
        except TimeoutException:
            break
    #print("Container:\n")
    #print(container)
    container1 = copy.deepcopy(container)
    sort_tennis_league(container1,key)
print(sorted_dict)
#//*[@id="3886"]/div/div[1]

driver.close()

def convert_data(data_dictionary):
    filename = 'betplanet_data_nfl.json'
    with open(filename, "w") as f:
        json.dump(data_dictionary, f, indent=4)

    f.close()

convert_data(sorted_dict)



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

        # loop to access dates[items] in scraped data
        for date in scraped_data:

            # create a dictionary[dict-2] for each date
            event_date = date
            event_dict = {}

            # create value/pair of date/new-dictionary[dict-2] in id-ed data dictionary[dict-1]
            # pass the array of events in each date to variable 
            data_dict[event_date] = event_dict
            event_arr = scraped_data[event_date]
    
            # create standard special string with day/month/league-abbreviation
            # from each date
            #event_date = event_date.replace(" ", "")
            special_str = ''
            key = event_date.find(" ")
            if key == 1:
                char_set_1 = event_date[0]
                char_set_1 = "0{}".format(char_set_1)
            elif key == 2:
                char_set_1 = event_date[0] + event_date[1]
            
            #char_set_x = event_date[2] + event_date[3] + event_date[4]
            #char_set_2 = event_date[-3] + event_date[-2] + event_date[-1]

            standard_string = char_set_1
            special_str = standard_string
            
            # get first two letters of home team and away team 
            # from each event in event array and add to special string
            for event_list in event_arr:
                home_team = event_list[1]
                away_team = event_list[3]
      
                home_team_break_points = home_team.split()
                home_team_key = max(home_team_break_points, key=len)
                home_team_ID = home_team_key[0] + home_team_key[1]

                away_team_break_points = away_team.split()
                away_team_key = max(away_team_break_points, key=len)
                away_team_ID = away_team_key[0] + away_team_key[1]

                #league_id = event_date[-3] + event_date[-2] + event_date[-1]

                special_str += home_team_ID.title() + away_team_ID.title() + 'nfl'

                # create value/pair of event-updated-special-string/event in
                # date/new-dictionary[dict-2]
                event_dict[special_str] = event_list

                # reset special string to standard string
                special_str = standard_string

        # update counter
        counter += 1
        #print(data_dict)

    # open scraped data file in write mode and 
    # update with new dictionary[dict-1]
    sorted_data = json_data
    with open(sorted_data, "w") as f:
        json.dump(data_dict, f, indent=4)
    f.close()

add_unique_keys('betplanet_data_nfl.json')