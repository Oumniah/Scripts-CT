#log in, works!

from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support.ui import Selects
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import re 

#Send message New code after outage
#Sends all links with description   ---> blocks when loading the page 
import pandas as pd
import numpy as np
import webbrowser
import urllib
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
import time
import tqdm 
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver

#get description of the link
from linkpreview import link_preview
from datetime import datetime


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



chrome_options = Options()
chrome_options.add_argument("user-data-dir=C:/Users/Administrateur/AppData/Local/Google/Chrome/User Data/Profile 1") 
#chrome_options.add_argument("--user-data-dir-Session")
#chrome_options.add_argument('--headless')
#chrome_options.add_argument('--incognito')   #to solve pop up showing problem but then can't reach the same driver again
chrome_options.add_argument("--disable-popup-blocking")
chrome_options.add_argument('--disable-notifications')
#chrome_options.add_argument("--profile-directory=Default")
chrome_options.add_experimental_option("detach", True)
chrome_options.add_experimental_option("excludeSwitches", ["disable-popup-blocking"])

##uncomment this only on the first run ---> keep same session open
driver_wtsp = webdriver.Chrome(executable_path='C:/Users/Administrateur/Desktop/Scripts/ReclamationsScript/chromedriver',options=chrome_options)

driver_wtsp.get("https://web.whatsapp.com/")



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
    
    #element_presence(By.XPATH, '//*[@id="main"]/footer/div[1]/div/div/div[2]/div[1]/div/div[2]', 40)
    #element_presence(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]', 40)
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





to_be_sent_df = pd.read_csv("C:/Users/Administrateur/Desktop/Scripts/ReclamationsScript/to_be_sent.csv")

now = datetime.now()
time_now = now.strftime("%d/%m/%Y %H:%M:%S")

if to_be_sent_df.empty == True :
    print(time_now)
    print("File is Empty")
    print("end of code")

else:
    print(time_now)
    print("File is not Empty")
    N_All_links_list = flatten_list(to_be_sent_df.values.tolist())

    
    #oumnia pro : +212666499291
    #oumnia: +2126930524451
    #soufiane : +212610205559
    phones = ['+212693052451']
    for i in range(0,len(phones)) :
        data = {'Link' :[N_All_links_list], 'Phone' :phones[i]}
        dummy2 = pd.DataFrame(data)
        print("right before send")
        prepare_msg(dummy2, 'Link', 'Phone')

        
N_All_links_list = []
data = {'Links to posts' : flatten_list(N_All_links_list)}
saved_links_df = pd.DataFrame(data)
saved_links_df.to_csv("C:/Users/Administrateur/Desktop/Scripts/ReclamationsScript/to_be_sent.csv", index=False)

driver_wtsp.close()