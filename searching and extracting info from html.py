# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 00:23:58 2022

@author: sriram
"""
import requests
from bs4 import BeautifulSoup

url = "https://webscraper.io/test-sites/e-commerce/allinone/phones/touch"
page = requests.get(url)
#print(page)

content_html = BeautifulSoup(page.text,"lxml")
#print(content_html)
#print(content_html.header.attrs)

price = content_html.find("h4",{"class":"pull-right price"}).text
#find object is usefull when you need to find something when it occurs first
#in the html file just like "content_html.header."[.] operator
#print(price)

#find all(finds all)
price_from_all = content_html.find_all("h4",class_ = "pull-right price")
#print(price_from_all)

#find_all part_2
all_tags = content_html.find_all(["h1","a"])
#print(all_tags)

if_attrs_exits = content_html.find_all(id=True)
#print(if_attrs_exits)

all_strings = content_html.find_all(string="Iphone")
#print(all_strings)

import re 
letter_start_with = content_html.find_all(string=re.compile("Iph"))
#print(letter_start_with)

getting_reviews_price = content_html.find_all(["h4","p"],class_=re.compile("pull-right"))
#print(getting_reviews_price)

first_three_of_r_p = content_html.find_all(["h4","p"],class_=re.compile("pull-right"),limit=4)
#print(first_three_of_r_p)

#find_all part 3 (press f9 to run cells without print)
product_names = content_html.find_all('a',class_="title")
product_names
prices = content_html.find_all("h4",class_="pull-right price")
prices
reviews = content_html.find_all("p",class_="pull-right")
reviews
description = content_html.find_all("p",class_="description")
description


def get_text_only(html_lines):
    text = []
    for i in html_lines:
        text.append(i.text)
    return text

product_names_list = get_text_only(product_names)
prices_list = get_text_only(prices)
reviews_list = get_text_only(reviews)
description_list = get_text_only(description)

import pandas as pd

Table = pd.DataFrame({"Product_names":product_names_list,
                      "Prices":prices_list,
                      "reviews":reviews_list,
                      "description":description_list})
Table


#Nested tag simplyfing
allvalue = content_html.find_all("div",class_="col-sm-4 col-lg-4 col-md-4")[0]
allvalue.find("h4",class_="pull-right price").text









