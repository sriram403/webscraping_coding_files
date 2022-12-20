# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 17:19:54 2022

@author: sriram
"""

from selenium import webdriver
driver = webdriver.Chrome("C:/chromedriver.exe")

driver.get("https://www.goat.com/collections/avant-garde-shapes")
#xpath
for i in range(1,10):
    prices = driver.find_element("xpath",'//*[@id="grid-body"]/div/div[1]/div['+str(i)+']/a/div[1]/div[2]/div/div[1]').text
    print(prices)
    
#keys 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome("C:/chromedriver.exe")
driver.get("https://www.google.co.in/")
box = driver.find_element("xpath","/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
box.send_keys("Im a bot google :)")
box.send_keys(Keys.ENTER)

#click
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome("C:/chromedriver.exe")
driver.get("https://www.google.co.in/")
box = driver.find_element("xpath","/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
box.send_keys("Im a bot google :)")
search_box = driver.find_element("xpath","/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[1]")
search_box.click()

#taking screenshot
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("C:/chromedriver.exe")
driver.get("https://www.google.co.in/")
box = driver.find_element("xpath","/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
box.send_keys("priyanka mohan")
box.send_keys(Keys.ENTER)
driver.find_element("xpath",'//*[@id="hdtb-msb"]/div[1]/div/div[2]/a').click()
driver.find_element("xpath",'//*[@id="islrg"]/div[1]/div[1]/a[1]/div[1]/img').screenshot("A:/Courses/Web_S_ing_in_Python_With_BeautifulSoup_and_Selenium/webscraping_coding_files/data's/first_pic.png")

#scrolling 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("C:/chromedriver.exe")
driver.get("https://www.google.co.in/")
box = driver.find_element("xpath","/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
box.send_keys("priyanka mohan")
box.send_keys(Keys.ENTER)
driver.find_element("xpath",'//*[@id="hdtb-msb"]/div[1]/div/div[2]/a').click()
driver.execute_script("return document.body.scrollHeight")
while True:
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

#wait two methods 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time 


driver = webdriver.Chrome("C:/chromedriver.exe")
driver.get("https://www.google.co.in/")
box = driver.find_element("xpath","/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
box.send_keys("priyanka mohan")
box.send_keys(Keys.ENTER)
driver.find_element("xpath",'//*[@id="hdtb-msb"]/div[1]/div/div[2]/a').click()
checking = WebDriverWait(driver,3).until(ec.presence_of_element_located((By.ID,'islr')))
#time.sleep(5)# do the same thing but without checking anything
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")








