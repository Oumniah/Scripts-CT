#loop works

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


#from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
#monExecutable = FirefoxBinary('C:/Users/ohoummi/Desktop/Python Scripts/Reclamations Script/geckodriver.exe')
#driver = webdriver.Firefox(firefox_binary= 'firefox.exe')
comments_list_all_posts = []
raw_data_list = []

options = webdriver.ChromeOptions()
options.add_argument('--disable-notifications')
driver = webdriver.Chrome('chromedriver.exe',options=options)
driver.get('https://www.facebook.com/casatram')
print("Facebook Opened...")
sleep(2)
#in case login page didn't open directly
button_connex = driver.find_element(By.XPATH,"//*[text()='Connexion']")   
button_connex.click()


email = driver.find_element_by_xpath("//input[@id='email' or @name='email']")
email.send_keys('ohoummi@casatramway.ma')
print("email entered...")
sleep(1)
password = driver.find_element_by_id("pass")
password.send_keys('serviceclients')
print("Password entered...")
sleep(1)
button = driver.find_element_by_xpath("//button[@id='loginbutton']")
button.click()
print("Page Opened...")
sleep(10)








old_comments = driver.find_element(By.XPATH,"//*[text()='Plus anciens']") 
#for x in range(0,10):
old_comments.click()
sleep(8)

all_comments = driver.find_element(By.XPATH,"//*[text()='Tous les commentaires']")
all_comments.click()
sleep(8)

#expand_comments = driver.find_element(By.XPATH,"//*/div[@class='oajrlxb2 bp9cbjyn g5ia77u1 mtkw9kbi tlpljxtp qensuy8j ppp5ayq2 goun2846 ccm00jje s44p3ltw mk2mc5f4 rt8b4zig n8ej3o3l agehan2d sk4xxmp2 rq0escxv nhd2j8a9 pq6dq46d mg4g778l btwxx1t3 g5gj957u p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x tgvbjcpo hpfvmrgz jb3vyjys p8fzw8mz qt6c0cv9 a8nywdso l9j0dhe7 i1ao9s8h esuyzwwr f1sip0of du4w35lb lzcic4wl abiwlrkh gpro0wi8 m9osqain buofh1pr']")
#expand_comments = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[4]/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/div/div/div/div/div/div/div[2]/div/div[4]/div/div/div[2]/div[4]/div/div[2]/span/span")
expand_comments = driver.find_element(By.XPATH,"//*[contains(text(),'autres commentaires')]") 
expand_comments.click()
sleep(8)
#end for
suite = driver.find_element(By.XPATH,"//*[text()='Afficher la suite']") 
sleep(8)
suite.click()
sleep(8)

comments_list_all_posts = driver.find_elements(By.XPATH,"//div[@class='cwj9ozl2 tvmbv18p']/ul/li")
for comment_list_all_posts in comments_list_all_posts :
    print(comment_list_all_posts.text)
    raw_data_list.append(comment_list_all_posts.text)

#test this in another workbook
data_list = []
for rows in raw_data_list :    
    row = rows.split('\n')
    print(row)
    if row[0] == 'Super fan':
            row = row[1:]
            data_list.append(row)

print("raw_data_list")
