# optimized : search+recent replaced by links
#optimized : search+recent replaced by links
#Soup

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
from tqdm import notebook
import time
#get description of the link
from linkpreview import link_preview
from datetime import datetime
from selenium.webdriver.remote.webdriver import WebDriver

words_list = ['Tram','Busway','Bus','باصواي','ترامواي','الطرام','طرام']

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

def attach_to_session(executor_url, session_id):
    original_execute = WebDriver.execute
    def new_command_execute(self, command, params=None):
        if command == "newSession":
            # Mock the response
            return {'success': 0, 'value': None, 'sessionId': session_id}
        else:
            return original_execute(self, command, params)
    # Patch the function before creating the driver object
    WebDriver.execute = new_command_execute
    driver = webdriver.Remote(command_executor=executor_url, desired_capabilities={})
    driver.session_id = session_id
    # Replace the patched function with original functions
    WebDriver.execute = original_execute
    return driver


comments_list_all_posts = []
raw_data_list = []
links_list = []
links_list1 = []  
All_links_list = []
New_All_links_list = []
time_list = []


url1 = pd.read_csv("C:/Users/Administrateur/Desktop/Scripts/ReclamationsScript/url_FB.csv")
url1 = flatten_list(url1.values.tolist())[0]
session_id = pd.read_csv("C:/Users/Administrateur/Desktop/Scripts/ReclamationsScript/session_id_FB.csv")
session_id = flatten_list(session_id.values.tolist())[0]


driver = attach_to_session(url1, session_id)
sleep(5)

print("Start")


driver.get('https://www.facebook.com/groups/480916455349909/search?q=Tramway&filters=eyJycF9jaHJvbm9fc29ydDowIjoie1wibmFtZVwiOlwiY2hyb25vc29ydFwiLFwiYXJnc1wiOlwiXCJ9In0%3D')

sleep(5)


#mouse hover to show links
element_to_hover_over = driver.find_element(By.CLASS_NAME,"oajrlxb2.g5ia77u1.qu0x051f.esr5mh6w.e9989ue4.r7d6kgcz.rq0escxv.nhd2j8a9.nc684nl6.p7hjln8o.kvgmc6g5.cxmmr5t8.oygrvhab.hcukyx3x.jb3vyjys.rz4wbd8a.qt6c0cv9.a8nywdso.i1ao9s8h.esuyzwwr.f1sip0of.lzcic4wl.gmql0nx0.gpro0wi8.b1v8xokw")

hover = ActionChains(driver).move_to_element(element_to_hover_over)
hover.perform()
sleep(3)
hover = ActionChains(driver).move_to_element(element_to_hover_over)
hover.perform()

sleep(3)
All_links_to_post = driver.find_elements(By.XPATH,"//a[@href]")

print('Tramway')
for link in All_links_to_post:
    #print(link.get_attribute("href"))
    links_list.append(link.get_attribute("href"))

All_links_list.append(links_list) #append to a list of lists
#key words list
words_list = ['Tram','Busway','Bus','باصواي','الطرام','ترامواي','طرام','الترامواي','الباصواي']
#words_list = ['Tram','Busway','Bus']
#words_list = ['Transport']


#Search Key words loop
for word in words_list :
    try :
        driver.get('https://www.facebook.com/groups/480916455349909/search?q='+word+'&filters=eyJycF9jaHJvbm9fc29ydDowIjoie1wibmFtZVwiOlwiY2hyb25vc29ydFwiLFwiYXJnc1wiOlwiXCJ9In0%3D')
        sleep(5)
        element_to_hover_over1 = driver.find_element(By.CLASS_NAME,"oajrlxb2.g5ia77u1.qu0x051f.esr5mh6w.e9989ue4.r7d6kgcz.rq0escxv.nhd2j8a9.nc684nl6.p7hjln8o.kvgmc6g5.cxmmr5t8.oygrvhab.hcukyx3x.jb3vyjys.rz4wbd8a.qt6c0cv9.a8nywdso.i1ao9s8h.esuyzwwr.f1sip0of.lzcic4wl.gmql0nx0.gpro0wi8.b1v8xokw")

        hover1 = ActionChains(driver).move_to_element(element_to_hover_over1)
        hover1.perform()
        sleep(3)
        hover1 = ActionChains(driver).move_to_element(element_to_hover_over1)
        hover1.perform()

        sleep(3)
        All_links_to_post1 = driver.find_elements(By.XPATH,"//a[@href]")
        print(word)
        for link in All_links_to_post1:
            #print(link.get_attribute("href"))
            links_list1.append(link.get_attribute("href"))
        All_links_list.append(links_list1)
    except :
        pass

print("Crawling done !")


#filter and delete comments

def Filter(datalist):
    # Search data based on regular expression in the list
    return [val for val in datalist
        if re.search(r'^https://www.facebook.com/groups/480916455349909/posts/', val)]

def Split(datalist):
    return [i.split('?', 1)[0] for i in datalist]

def delete_comments(datalist):
    return [val for val in datalist
    if re.search(r'^((?!comment_id).)*$', val)]


# Filter the list of the first keyword
links_list = Filter(links_list)
links_list = delete_comments(links_list)
links_list = Split(links_list)

# Filter the list of the rest of the keywords
for l in All_links_list :
    l = Filter(l)
    l = delete_comments(l)
    l = Split(l)
    #if l not in saved_link_reste ://////////////
    New_All_links_list.append(l)

#turn a list of list to a simple list 
New_All_links_list = flatten_list(New_All_links_list)
#set to drop duplicate
New_All_links_list = list(set(New_All_links_list)) 
print("filtering and flattering done !")

##do it only on the first time 
#saved_links = New_All_links_list


#get Only new posts

#load old links from file
saved_links_df = pd.read_csv("C:/Users/Administrateur/Desktop/Scripts/ReclamationsScript/saved_links.csv")
saved_links = flatten_list(saved_links_df.values.tolist())


def Diff(li1, li2):
    return list(set(li1) - set(li2))
 
N_All_links_list =  Diff(New_All_links_list,saved_links)

#save the result into a list
now = datetime.now()
time_now = now.strftime("%d/%m/%Y %H:%M:%S")
time_list = [time_now]
saved_links.append(time_list)
saved_links.append(N_All_links_list)
N_All_links_list #this is the list to send via whatsapp 


#save the results to a file (old links)

data = {'Links to posts' : flatten_list(saved_links)}
saved_links_df = pd.DataFrame(data)
saved_links_df.to_csv("C:/Users/Administrateur/Desktop/Scripts/ReclamationsScript/saved_links.csv", index=False)
saved_links_df.to_csv("C:/Users/Administrateur/Desktop/Scripts/ReclamationsScript/saved_links_backup.csv", index=False)

#save the results to a file ( to be sent)

data = {'Links to posts' : flatten_list(N_All_links_list)}
saved_links_df = pd.DataFrame(data)
saved_links_df.to_csv("C:/Users/Administrateur/Desktop/Scripts/ReclamationsScript/to_be_sent.csv", index=False)

print("end of script")


