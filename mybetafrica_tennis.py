# -*- coding: utf-8 -*-
"""

Created on Wed Aug 25 11:37:36 2021

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
wait2 = WebDriverWait(driver,15)


url_code = ""
league_name = []
datetime_list = []
datetime_list1 = []
event_info_list_section = []
event_info_list_section1 = []
event_info_list_total = []
event_info_list_total1 = []
current_url = []


def write_to_csv(y):
    filename = "sorted_mybetafrica_tennis.csv"
    with open(filename,'w') as csvfile:
    # creating a csv writer object
        csvwriter = csv.writer(csvfile)
        fields = ['Team1','Team2','odd1','odd2','date','league']
    
      # writing the fields
        csvwriter.writerow(fields)
    
     # writing the data rows
    
        csvwriter.writerows(y)
        print("csv File created")

filename = "mybet.json"
s = ['https://www.mybet.africa/sport/odds?tournaments=251749&timeFrame=all']

with open(filename) as f:
    data = json.load(f)
# Original json loop
for l,value in data.items():
    url_code = url_code + "-" + value
    url_code = value
#u = ['354030', '224088', '232804', '330216', '283911', '350005', '354037']

#for url_code in u:


    
   # url_code = url_code[1:]

    print(url_code)

    url = "https://www.mybet.africa/sport/odds?tournaments={}&timeFrame=all".format(url_code)

    driver.get(url)
#for l in s:
    #driver.get(l)
    no_tournament_path = '//*[@id="nvsOddsPage"]/nvs-no-data-info/div/div/p'
    try:
        no_tournament = wait2.until(EC.presence_of_element_located((By.XPATH,no_tournament_path)))
        
    except:
        flag1 =True
        counter = 1
        current_url.append(url_code)
        
        while flag1:
            try:
                league_xpath = '//*[@id="nvsOddsPage"]/div/div[{}]/div[1]/div[2]/h1/span'.format(counter)
                league_type = wait.until(EC.presence_of_element_located((By.XPATH,league_xpath)))
                league_name.append(league_type.text)
                datetime_xpath = '//*[@id="nvsOddsPage"]/div/div[{}]/div[4]/div/nvs-odds-table/div/div[2]/div[1]/div[1]/h3/nvs-configure-date-time-for-view'.format(counter)
        
                 
                datetime = wait.until(EC.presence_of_element_located((By.XPATH,datetime_xpath)))
                datetime_list.append(datetime.text)
                
                event_info_xpath ='//*[@id="nvsOddsPage"]/div/div[{}]/div[4]/div/nvs-odds-table/div/div[2]/div[3]'.format(counter)
                event_info_xpath_1 = '//*[@id="nvsOddsPage"]/div/div[{}]/div[4]/div/nvs-odds-table/div/div[3]/div[3]'.format(counter)
                event_info = wait.until(EC.presence_of_element_located((By.XPATH,event_info_xpath)))
                try:
                    datetime_xpath1='//*[@id="nvsOddsPage"]/div/div/div[4]/div/nvs-odds-table/div/div[3]/div[1]/div[1]/h3/nvs-configure-date-time-for-view'
                   
              
                    datetime1 = wait.until(EC.presence_of_element_located((By.XPATH,datetime_xpath1)))
                    datetime_list1.append(datetime1.text)
                 
                    event_info1 = wait.until(EC.presence_of_element_located((By.XPATH,event_info_xpath_1)))
                    event_info_list_section1 = (event_info1.text).split("\n")
                    event_info_list_section1.append(league_type.text)
                    event_info_list_section1.append(datetime1.text)
                    event_info_list_total1.append(event_info_list_section1)
                   
                except TimeoutException:
                    pass
                event_info_list_section = (event_info.text).split("\n")             
                event_info_list_section.append(league_type.text)
                event_info_list_section.append(datetime.text)
                event_info_list_total.append(event_info_list_section)
             
                counter = counter + 1
            except TimeoutException:
                break

#Preprocessing the information
def preprocess(list):
    temp_b = []
    for l in list:
        temp_a = []
        counter = 0
        #print("lenl ",len(l))
        for i,v in enumerate(l):
            if (v[0].isalpha() and (i != (len(l) - 2) and (i != (len(l) - 1) ))):
                inde = l.index(v)
         #       print(inde)
          #      print("i:",i)
           #     print("e",len(l) - 2 )
                temp_a = [l[inde - 1],l[inde],l[inde + 1],l[inde + 2],l[-2],l[-1]]
            #    print("count:",counter)
             #   print("v",v)
                counter = counter + 1
                temp_b.append(temp_a)
                temp_a = []
            if counter == 2:
                counter = 0
    return temp_b
      

print("\n")
print(event_info_list_total)
# calling preproces function
first_list = preprocess(event_info_list_total)

second_list = preprocess(event_info_list_total1)

# 
for i in second_list:
    first_list.append(i)
    
    
print(first_list)
write_to_csv(first_list)


#print(event_info_list_total)
#print("\n")
#print(event_info_list_total1)
#print(league_name)
#print(datetime_list)
#print("\n")
#print(datetime_list1)
#print("\n")
#print("url code",current_url)
