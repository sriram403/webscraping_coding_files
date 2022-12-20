# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 17:19:54 2022

@author: sriram
"""

from selenium import webdriver
driver = webdriver.Chrome("C:/chromedriver.exe")

driver.get("https://www.goat.com/collections/avant-garde-shapes")
driver.find_element("xpath",'//*[@id="grid-body"]/div/div[1]/div[2]/a/div[1]/div[2]')
for i in range(1,10):
    prices = driver.find_element("xpath",'//*[@id="grid-body"]/div/div[1]/div['+str(i)+']/a/div[1]/div[2]/div/div[1]').text
    print(prices)
