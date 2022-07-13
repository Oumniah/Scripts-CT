#Pull the results from the file 

#log in, works!

from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import re 

#Send message New code after outage
#Sends all links with description   ---> blocks when loading the page 
import os
import pandas as pd
import numpy as np
import webbrowser
from selenium import webdriver
import urllib
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
import tqdm
import time
#get description of the link
from linkpreview import link_preview


#flatteren list to delete duplicates

def flatten_list(_2d_list):
    flat_list = []
    # Iterate through the outer list
    for element in _2d_list:
        if type(element) is list:
            # If the element is of type list, iterate through the sublist
            for item in element:
                flat_list.append(item)
        else:
            flat_list.append(element)
    return flat_list


#send message via wtsp functions
def element_presence(by, xpath, time):
    print("element presence")
    element_present = EC.presence_of_element_located((By.XPATH, xpath))
    WebDriverWait(driver_wtsp, time).until(element_present)
    
def send_message(url):
    print("send message")
    driver_wtsp.get(url)
    time.sleep(3) 
    #element_presence(By.XPATH, '//*[@id="main"]/footer/div[1]/div/div/div[2]/div[1]/div/div[2]', 40)
    element_presence(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]', 40)
    msg_box = driver_wtsp.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')
    print("made it through element presence !")
    time.sleep(3)
    msg_box.send_keys('\n')    

def prepare_msg(dataframe, link_col ,phone_col):
    print("prepare message")
    file = dataframe[[link_col, phone_col]]
    base_msg = """
{}
{}


--Ce message est envoyé par un robot automatique--
"""
    base_url = 'https://web.whatsapp.com/send?phone={}&text={}'
    for i,j in tqdm.tqdm(file.iterrows()):
        phone_no = j[phone_col]
        Link = j[link_col]
        for i in range(0,len(Link)):
            msg = urllib.parse.quote(base_msg.format(link_preview(Link[i]).description,Link[i]))
            url_msg = base_url.format(phone_no, msg)
            send_message(url_msg)
            sleep(2)




to_be_sent_df = pd.read_csv("C:/Users/ohoummi/Desktop/Scripts/ReclamationsScript/to_be_sent.csv")

if to_be_sent_df.empty == True :
    print("File is Empty")
else:
    print("File is not Empty")
    
    N_All_links_list = flatten_list(to_be_sent_df.values.tolist())
              
    chrome_options = Options()
    chrome_options.add_argument("--user-data-dir-Session")
    #chrome_options.add_argument('--incognito')   #to solve pop up showing problem but then can't reach the same driver again
    #chrome_options.add_argument("--disable-popup-blocking")
    #chrome_options.add_argument('--disable-notifications')
    chrome_options.add_argument("--profile-directory=Default")
    #chrome_options.add_experimental_option("detach", True)
    chrome_options.add_experimental_option("excludeSwitches", ["disable-popup-blocking"])

    PATH = "C:/Users/ohoummi/Desktop/Scripts/ReclamationsScript/chromedriver.exe"
    ##uncomment this only on the first run ---> keep same session open
    driver_wtsp = webdriver.Chrome(PATH, options=chrome_options)

    #for i in range(0,len(New_All_links_list)) :
    data = {'Link' :[N_All_links_list], 'Phone' :['+212666499291']}
    dummy2 = pd.DataFrame(data)
    prepare_msg(dummy2, 'Link', 'Phone')

   
	