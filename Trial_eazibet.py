
#//*[@id="content-container"]/div/home-page/section/div/games-list/div/gamelist/div/div/div[10]/game/div/div
#//*[@id="content-container"]/div/home-page/section/div/games-list/div/gamelist/div/div/div[10]/game/div/market-list/div/div[1]/div/div

from selenium.common.exceptions import NoSuchElementException,StaleElementReferenceException,TimeoutException   
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import json
#import tra



options = webdriver.ChromeOptions()
options.add_argument("start-maximized")

driver = webdriver.Chrome(executable_path='chromedriver.exe',options=options)
wait = WebDriverWait(driver,10)
forbi = []


odds_xpath = '//*[@id="content-container"]/div/home-page/section/div/games-list/div/gamelist/div/div/div[20]/game/div/market-list/div/div[1]/div[1]'

driver.get("https://www.eazibet.com.gh/en/tennis/tennis-wta-us-open-new-york-usa")

#no_avail_xpath = '//*[@id="content-container"]/div/home-page/section/div/games-list/div/gamelist/div/div/div[10]/game/div/market-list/div/div[1]/div/div'
no_avail = wait.until(EC.presence_of_element_located((By.XPATH,odds_xpath)))
#no_avail = driver.find_element_by_xpath(no_avail_xpath)

def get_nolink():
    print(no_avail.text)
    Lengt = 20 + 1
    i = 1
    while i < Lengt:
        v = '//*[@id="content-container"]/div/home-page/section/div/games-list/div/gamelist/div/div/div[{}]/game/div/market-list/div/div[1]/div[1]'.format(i)
        avail = wait.until(EC.presence_of_element_located((By.XPATH,v)))
        print(v)
        if avail.text == "Click to show available odds":
            k = i
        
            i = i + 1
    return k
    