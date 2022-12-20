# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 13:24:24 2022

@author: sriram
"""

import requests 
from bs4 import BeautifulSoup

url = "https://www.marketwatch.com/investing/stock/tsla?mod=search_symbol"

page = requests.get(url)
page

soup = BeautifulSoup(page.text,"lxml")
soup

#finding the price 
all_price = soup.find_all("bg-quote",{"field":"Last"},class_="value")[0]
price = all_price.text
price

#closing price
all_closing_price = soup.find_all("div",class_="intraday__close")[0]
closing_price = all_closing_price.find("td",class_="table__cell u-semi").text
closing_price

#52 weeks range 
all_range = soup.find_all("div",class_="range__header")[2]
range_price_all = all_range.find_all("span",class_="primary")
range_price_start = range_price_all[0].text
range_price_end = range_price_all[1].text
range_price_start,range_price_end

#rating 
all_rating = soup.find_all("div",class_="analyst__chart")[0]
rating_active = all_rating.find_all("li",class_="analyst__option active")[0]
rating = rating_active.text
rating_active

import pandas as pd
dataframe = pd.DataFrame({"Price":"$"+price,
                          "closing_price":closing_price,
                          "range_start":range_price_start,
                          "range_end":range_price_end,
                          "rating":rating},index=[0])
dataframe