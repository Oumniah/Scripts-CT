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
from selenium import webdriver
import urllib
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
import time
import tqdm 

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

url1 = driver_wtsp.command_executor._url   
session_id = driver_wtsp.session_id 

#store sesssion_id
session_id_list = [session_id]
data_session_id = {'session_id' : session_id_list}
session_id_df = pd.DataFrame(data_session_id)
session_id_df.to_csv("C:/Users/Administrateur/Desktop/Scripts/ReclamationsScript/session_id.csv", index=False)

url_list = [url1]
data_url = {'url' : url_list }
url_df = pd.DataFrame(data_url)
url_df.to_csv("C:/Users/Administrateur/Desktop/Scripts/ReclamationsScript/url.csv", index=False)
