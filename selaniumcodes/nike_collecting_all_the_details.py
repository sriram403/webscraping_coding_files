import requests 
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import pandas as pd

driver = webdriver.Chrome("C:/chromedriver.exe")
driver.get("https://www.nike.com/in/w/mens-clothing-6ymx6znik1")
time.sleep(5)
p_s_h = driver.execute_script("return document.body.scrollHeight")
c_s_h = p_s_h+1
while  p_s_h != c_s_h:
    p_s_h = driver.execute_script("return document.body.scrollHeight")
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(2)
    c_s_h = driver.execute_script("return document.body.scrollHeight")
print("finished_scrolling :)")
soup = BeautifulSoup(driver.page_source,"lxml")
all_thumbnails = soup.find_all("div",class_="product-card__body")
len(all_thumbnails)
all_thumbnails[23].find("div",class_="product-price in__styling is--current-price css-11s12ax").text
df = pd.DataFrame(columns=["link","name","desc","rate"])
print("starting to filling the data :)")
for i,post in enumerate(all_thumbnails):
    try:
        link = post.find("a",class_="product-card__link-overlay").get("href")
        name = post.find("a",class_="product-card__link-overlay").text
        desc = post.find("div",class_="product-card__subtitle").text
        rate = post.find("div",class_="product-price in__styling is--current-price css-11s12ax").text
        df = pd.concat([df,pd.DataFrame({df.columns[0]:link,df.columns[1]:name,df.columns[2]:desc,df.columns[3]:rate},index=[0])],ignore_index=True)
    except:
        pass
print("finished...")
    
    