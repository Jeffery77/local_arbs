# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 06:25:50 2020

@authors: Duke Young, M. Chase
"""


from selenium.common.exceptions import NoSuchElementException,StaleElementReferenceException,TimeoutException   
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import copy
import json


sorted_dict = {}
# method to sort date time and odds of 3 way odds.
def sort_match_date_odd(list,key):
    start = 0
   
   
    length_of_z = len(list) - 1




    while (start < length_of_z):
        flag  = True
        #print(start)
        #print(z)
  
        first_date = list.pop(0)

        print(first_date)
        day = first_date.pop(0)
        month = first_date.pop(0)
        if day == "OUTRIGHT":
            start = start + 1
            continue
        #Removing live matches from the list ; expand code later
        if day == "IN-PLAY":
            start = start + 1
            continue

        first_date_date = day + " "  + month
        print(first_date_date)
        # Removing match result in the list
        first_date.pop(0)
        # Removing the first 7 elements 
        #print(first_date)
        li = []
        z1 = []
        wanted = [0,1,2,3,4,5,6]
        while flag:
            try:
                for ele in sorted(wanted,reverse=True):
                    y=(first_date.pop(ele))
                    #delete the weird number
            
            
                    # print("Y is :",y)
               
                
                    li.append(y)
                first_date.pop(0)
                #print("batch:")
                #print(first_date)
                z1.append(li)
                #print("This is " + str(i))
                li = []
                #print(first_date)

               # i += 1
            except IndexError:
                flag = False
        
        start = start + 1
        #print(z1)
        if z1 in sorted_dict.values():
            pass
        else:
            sorted_dict[first_date_date + key] = z1
            #print("sorted dictionary")
            #print(sorted_dict)


options = webdriver.ChromeOptions()
options.add_argument("start-maximized")

driver = webdriver.Chrome(executable_path='chromedriver.exe',options=options)
wait = WebDriverWait(driver,20)

container = []
container1 = []

Soccer_league_types ={'la-liga-spl':['https://sports.betplanet.com.gh/home/wrapper/events?list=%5B%7B%22sport%22:1,%22leagues%22:%5B1831%5D%7D%5D','1831'],'English-premier-league-epl':['https://sports.betplanet.com.gh/home/wrapper/events?list=%5B%7B%22sport%22:1,%22leagues%22:%5B1627%5D%7D%5D','1627']}



for key,value in Soccer_league_types.items():
    i = 1
    driver.get(value[0])
    while True:
        
        try:
            match_string = '//*[@id="{}"]/div/div[{}]'.format(value[1],i)
            matches = wait.until(EC.presence_of_element_located((By.XPATH,match_string)))
            matches = matches.get_attribute('innerText')
            final_matches = matches.split('\n')
            container.append(final_matches)
            
            i = i + 1
        except IndexError:
            break
        except TimeoutException:
            break
        

   # print(key)
    container1 = copy.deepcopy(container)
    sort_match_date_odd(container1,key)  
    #print('Done')
    #print("sorted dictionary")
#print(sorted_dict)

def convert_data(data_dictionary):
    filename = 'betplanet_data.json'
    with open(filename, "w") as f:
        json.dump(data_dictionary, f, indent=4)

    f.close()

convert_data(sorted_dict)

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
                away_team = event_list[5]
      
                home_team_break_points = home_team.split()
                home_team_key = max(home_team_break_points, key=len)
                home_team_ID = home_team_key[0] + home_team_key[1]

                away_team_break_points = away_team.split()
                away_team_key = max(away_team_break_points, key=len)
                away_team_ID = away_team_key[0] + away_team_key[1]

                league_id = event_date[-3] + event_date[-2] + event_date[-1]

                special_str += home_team_ID.title() + away_team_ID.title() + league_id

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

add_unique_keys('betplanet_data.json')