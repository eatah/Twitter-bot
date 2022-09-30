from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import common
from selenium.common.exceptions import NoSuchElementException
import time
import re



browser = webdriver.Firefox()
browser.get('https://twitter.com/i/flow/login')
time.sleep(4)
browser.find_element(By.CLASS_NAME, "r-30o5oe").send_keys("leapyfrawgers@gmail.com" + Keys.ENTER)
time.sleep(4)
browser.find_element(By.CLASS_NAME, "r-30o5oe").send_keys("2154595493" + Keys.ENTER)
time.sleep(4)
browser.find_element(By.NAME, "password").send_keys("#Frawgers" + Keys.ENTER)
time.sleep(4)
browser.get('https://twitter.com/piovincenzo_/followers')
#browser.find_element(By.CLASS_NAME, "r-30o5oe").send_keys("#nfts" + Keys.ENTER)
time.sleep(4)

for x in range(20):
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);") 
    time.sleep(5)
            #browser.find_element(By.XPATH, "//div[@class='css-18t94o4 css-1dbjc4n r-42olwf r-sdzlij r-1phboty r-rs99b7 r-15ysp7h r-4wgw6l r-1ny4l3l r-ymttw5 r-o7ynqc r-6416eg r-lrvibr']").click()
   

i=10
while i>0: 
   
    for x in range(50):
        
        try:     
            browser.find_element(By.XPATH, "//div[@class='css-18t94o4 css-1dbjc4n r-42olwf r-sdzlij r-1phboty r-rs99b7 r-15ysp7h r-4wgw6l r-1ny4l3l r-ymttw5 r-o7ynqc r-6416eg r-lrvibr']").click()
            time.sleep(5)
        except NoSuchElementException: 
            browser.execute_script('window.scrollTo(0,document.body.scrollHeight/1.5)') 
            browser.execute_script('window.scrollTo(0,document.body.scrollHeight/1.5)')
            time.sleep(5)
            browser.find_element(By.XPATH, "//div[@class='css-18t94o4 css-1dbjc4n r-42olwf r-sdzlij r-1phboty r-rs99b7 r-15ysp7h r-4wgw6l r-1ny4l3l r-ymttw5 r-o7ynqc r-6416eg r-lrvibr']").click()
    time.sleep(1080)
    for x in range(50):
        
    
        try:     
            browser.find_element(By.XPATH, "//div[@class='css-18t94o4 css-1dbjc4n r-42olwf r-sdzlij r-1phboty r-rs99b7 r-15ysp7h r-4wgw6l r-1ny4l3l r-ymttw5 r-o7ynqc r-6416eg r-lrvibr']").click()
            time.sleep(5)
        except NoSuchElementException: 
            browser.execute_script('window.scrollTo(0,document.body.scrollHeight/1.5)') 
            browser.execute_script('window.scrollTo(0,document.body.scrollHeight/1.5)')
            time.sleep(5)
            browser.find_element(By.XPATH, "//div[@class='css-18t94o4 css-1dbjc4n r-42olwf r-sdzlij r-1phboty r-rs99b7 r-15ysp7h r-4wgw6l r-1ny4l3l r-ymttw5 r-o7ynqc r-6416eg r-lrvibr']").click()
    time.sleep(1080)
    for x in range(50):
        
        try:     
            browser.find_element(By.XPATH, "//div[@class='css-18t94o4 css-1dbjc4n r-42olwf r-sdzlij r-1phboty r-rs99b7 r-15ysp7h r-4wgw6l r-1ny4l3l r-ymttw5 r-o7ynqc r-6416eg r-lrvibr']").click()
            time.sleep(5)
        except NoSuchElementException: 
            browser.execute_script('window.scrollTo(0,document.body.scrollHeight/1.5)') 
            time.sleep(5)
            browser.find_element(By.XPATH, "//div[@class='css-18t94o4 css-1dbjc4n r-42olwf r-sdzlij r-1phboty r-rs99b7 r-15ysp7h r-4wgw6l r-1ny4l3l r-ymttw5 r-o7ynqc r-6416eg r-lrvibr']").click()
    time.sleep(1080)
    
    browser.get('https://twitter.com/Morphies_nft/following')
    
    for x in range(150):
        
        try:     
            browser.find_element(By.XPATH, "//div[@class='css-18t94o4 css-1dbjc4n r-42olwf r-sdzlij r-1phboty r-rs99b7 r-15ysp7h r-4wgw6l r-1ny4l3l r-ymttw5 r-o7ynqc r-6416eg r-lrvibr']").click()
            time.sleep(5)
        except NoSuchElementException: 
            browser.execute_script('window.scrollTo(0,document.body.scrollHeight/1.5)') 
            time.sleep(5)
            browser.find_element(By.XPATH, "//div[@class='css-18t94o4 css-1dbjc4n r-42olwf r-sdzlij r-1phboty r-rs99b7 r-15ysp7h r-4wgw6l r-1ny4l3l r-ymttw5 r-o7ynqc r-6416eg r-lrvibr']").click()
    time.sleep(1080)
    for x in range(150):
        
        try:     
            browser.find_element(By.XPATH, "//div[@class='css-18t94o4 css-1dbjc4n r-42olwf r-sdzlij r-1phboty r-rs99b7 r-15ysp7h r-4wgw6l r-1ny4l3l r-ymttw5 r-o7ynqc r-6416eg r-lrvibr']").click()
            time.sleep(5)
        except NoSuchElementException: 
            browser.execute_script('window.scrollTo(0,document.body.scrollHeight/1.5)') 
            time.sleep(5)
            browser.find_element(By.XPATH, "//div[@class='css-18t94o4 css-1dbjc4n r-42olwf r-sdzlij r-1phboty r-rs99b7 r-15ysp7h r-4wgw6l r-1ny4l3l r-ymttw5 r-o7ynqc r-6416eg r-lrvibr']").click()
    time.sleep(1080)
    for x in range(150):
        
        try:     
            browser.find_element(By.XPATH, "//div[@class='css-18t94o4 css-1dbjc4n r-42olwf r-sdzlij r-1phboty r-rs99b7 r-15ysp7h r-4wgw6l r-1ny4l3l r-ymttw5 r-o7ynqc r-6416eg r-lrvibr']").click()
            time.sleep(5)
        except NoSuchElementException: 
            browser.execute_script('window.scrollTo(0,document.body.scrollHeight/1.5)') 
            time.sleep(5)
            browser.find_element(By.XPATH, "//div[@class='css-18t94o4 css-1dbjc4n r-42olwf r-sdzlij r-1phboty r-rs99b7 r-15ysp7h r-4wgw6l r-1ny4l3l r-ymttw5 r-o7ynqc r-6416eg r-lrvibr']").click()
    time.sleep(86400)
