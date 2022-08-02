#no links appearing problems
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

#import seaborn as sns
#import matplotlib.pyplot as plt
            

#from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
#monExecutable = FirefoxBinary('C:/Users/ohoummi/Desktop/Python Scripts/Reclamations Script/geckodriver.exe')
#driver = webdriver.Firefox(firefox_binary= 'firefox.exe')


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
driver.get('https://www.facebook.com/groups/480916455349909')
print("Group Oppened...")
time.sleep(5) 




#Search first Key word
search_button = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[3]/div/div/div[2]/div[2]/div/div/div[1]/div")
search_button.click()
sleep(8)
#search_button = driver.find_element_by_xpath("//button[@id='mount_0_0_CH']")
#search_button = driver.find_element_by_id("mount_0_0_CH")
#search_button = driver.find_element_by_xpath("//div[@class='oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 pq6dq46d p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl n00je7tq arfg74bv qs9ysxi8 k77z8yql l9j0dhe7 abiwlrkh p8dawk7l cbu4d94t taijpn5t k4urcfbm']")
input_search = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/div/div/label/input")
sleep(3)
input_search.send_keys('Tramway')
sleep(3)

input_search.send_keys('\n')
#search_keyword = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/ul/li/ul/li[7]/div/div[1]/div")
#search_keyword.click()
sleep(5)

#activate recent posts button
recent_posts_button = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div[2]/div/div[3]/div/div[2]/div/div[2]/div/input")
sleep(5)
driver.execute_script("arguments[0].click()",recent_posts_button)

    
#recent_posts_button = driver.find_element_by_css_selector("input.oajrlxb2.rq0escxv.f1sip0of.hidtqoto.nhd2j8a9.datstx6m.kvgmc6g5.cxmmr5t8.oygrvhab.hcukyx3x.b5wmifdl.lzcic4wl.jb3vyjys.rz4wbd8a.qt6c0cv9.a8nywdso.pmk7jnqg.j9ispegn.kr520xx4.k4urcfbm").click();
#recent_posts_button = driver.find_element_by_css_selector("input[area-label='Plus récentes']").click();
sleep(5)

#collect links nad append them to a list


#mouse hover to show links
element_to_hover_over = driver.find_element(By.CLASS_NAME,"oajrlxb2.g5ia77u1.qu0x051f.esr5mh6w.e9989ue4.r7d6kgcz.rq0escxv.nhd2j8a9.nc684nl6.p7hjln8o.kvgmc6g5.cxmmr5t8.oygrvhab.hcukyx3x.jb3vyjys.rz4wbd8a.qt6c0cv9.a8nywdso.i1ao9s8h.esuyzwwr.f1sip0of.lzcic4wl.gmql0nx0.gpro0wi8.b1v8xokw")
sleep(5)
hover = ActionChains(driver).move_to_element(element_to_hover_over)
sleep(3)
hover.perform()
sleep(2)
All_links_to_post = driver.find_elements_by_xpath("//a[@href]")
    
#All_links_to_post = driver.find_elements_by_xpath("//a[contains(@class,'oajrlxb2.g5ia77u1.qu0x051f.esr5mh6w.e9989ue4.r7d6kgcz.rq0escxv.nhd2j8a9.nc684nl6.p7hjln8o.kvgmc6g5.cxmmr5t8.oygrvhab.hcukyx3x.jb3vyjys.rz4wbd8a.qt6c0cv9.a8nywdso.i1ao9s8h.esuyzwwr.f1sip0of.lzcic4wl.gmql0nx0.gpro0wi8.b1v8xokw')]")
#All_dates_to_post = driver.find_elements_by_xpath("/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[4]/div/div/div/div/div/div/div[4]/div/div/div/div/div/div[3]/a/div[1]/div/div[1]/div/div[1]/span/span/span").getText()
#All_links_to_post = driver.find_elements(By.CLASS_NAME,"oajrlxb2.g5ia77u1.qu0x051f.esr5mh6w.e9989ue4.r7d6kgcz.rq0escxv.nhd2j8a9.nc684nl6.p7hjln8o.kvgmc6g5.cxmmr5t8.oygrvhab.hcukyx3x.jb3vyjys.rz4wbd8a.qt6c0cv9.a8nywdso.i1ao9s8h.esuyzwwr.f1sip0of.lzcic4wl.gmql0nx0.gpro0wi8.b1v8xokw")


print('Tramway')
for link in All_links_to_post:
    print(link.get_attribute("href"))
    links_list.append(link.get_attribute("href"))

All_links_list.append(links_list) #append to a list of lists
#key words list
words_list = ['Tram','Busway','Bus','باصواي','ترامواي','Transport']
#words_list = ['Tram','Busway','Bus']
#words_list = ['Transport']

#Search Key words loop
for word in words_list :
    input_search1 = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[3]/div[1]/div[2]/div/div/div/div/label/input")
    sleep(6) 
    input_search1.send_keys((Keys.CONTROL, 'a'), Keys.BACKSPACE) #Clear old key search word to replace it
    input_search1.send_keys(word)
    sleep(5)
    input_search1.send_keys(Keys.ENTER);
    #input_search1.click()
    sleep(5)
    #search_keyword1 = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[2]/div/div/div[1]/div[1]/div/ul/li/ul/li[7]/div/div[1]/div")
    #search_keyword1.send_keys(Keys.ENTER)
    #search_keyword1.click()
    #sleep(3)
    recent_posts_button1 = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div[2]/div/div[3]/div/div[2]/div/div[2]/div/input")
    sleep(5)
    driver.execute_script("arguments[0].click()",recent_posts_button1)
    
    
    #click on post to show link
    
    #first_post_link = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[4]/div/div/div/div/div/div/div[4]/div/div/div/div/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div[2]/div/div[2]/span/span/span[2]/span/a")
    #sleep(3)
    #try :
    #    driver.execute_script("arguments[0].click()",first_post_link)
    #except :
    #    driver.execute_script("arguments[0].click()",first_post_link)
    sleep(5)
    #collect links nad append them to a list
    print(word)
    #collect links nad append them to a list
    #mouse hover to show links
    element_to_hover_over1 = driver.find_element(By.CLASS_NAME,"oajrlxb2.g5ia77u1.qu0x051f.esr5mh6w.e9989ue4.r7d6kgcz.rq0escxv.nhd2j8a9.nc684nl6.p7hjln8o.kvgmc6g5.cxmmr5t8.oygrvhab.hcukyx3x.jb3vyjys.rz4wbd8a.qt6c0cv9.a8nywdso.i1ao9s8h.esuyzwwr.f1sip0of.lzcic4wl.gmql0nx0.gpro0wi8.b1v8xokw")
    hover1 = ActionChains(driver).move_to_element(element_to_hover_over1)
    hover1.perform()
    sleep(3)
    All_links_to_post1 = driver.find_elements_by_xpath("//a[@href]")
    for link in All_links_to_post1:
        #print(link.get_attribute("href"))
        links_list1.append(link.get_attribute("href"))
    All_links_list.append(links_list1)
    

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