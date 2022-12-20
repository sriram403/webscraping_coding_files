import requests
import pandas as pd
from bs4 import BeautifulSoup
url = "https://www.carpages.ca/used-cars/search/?fueltype_id%5B0%5D=3&fueltype_id%5B1%5D=7"
page = requests.get(url)
soup = BeautifulSoup(page.text,"lxml")

all_thumbnails = soup.find_all("div",class_="media soft push-none rule")
df= pd.DataFrame(columns=["Link","Name","Price","Color"])
pages = 0
while pages<=15:
    pages+=1
    for post in all_thumbnails:
        try:
            name = post.find("h4",class_="hN").text.strip()
            h_l  = post.find("h4",class_="hN").find("a").get("href")
            full_link = "https://www.carpages.ca/"+h_l
            price = post.find("div",class_="l-column l-column--medium-4 push-none").text.strip()
            color = post.find_all("div",class_="grey l-column l-column--small-6 l-column--medium-4")[1].find("span").text.strip()
            df = pd.concat([df,pd.DataFrame({df.columns[0]:full_link,df.columns[1]:name,df.columns[2]:price,df.columns[3]:color},index=[0])],ignore_index=True)
        except:
            pass
    half_url = soup.find("a",{"title":"Next Page"}).get("href")
    full_url = "https://www.carpages.ca/"+half_url
    page = requests.get(full_url)
    soup = BeautifulSoup(page.text,"lxml")
    all_thumbnails = soup.find_all("div",class_="media soft push-none rule")
df.to_csv("A:/Courses/Web_S_ing_in_Python_With_BeautifulSoup_and_Selenium/webscraping_coding_files/data's/car.csv",index=False)
  
