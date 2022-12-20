# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 14:43:27 2022

@author: sriram
"""

import requests,pandas as pd
from bs4 import BeautifulSoup

url = "https://www.worldometers.info/world-population/"
page = requests.get(url)
soup = BeautifulSoup(page.text,"lxml")

table_comp = soup.find_all("div",class_="table-responsive")
table_comp
table_header_all = table_comp[0].find_all("th")
table_header_all

def get_text(html_lines):
    text = []
    for i in html_lines:
        text.append(i.text)
    return text

headers = get_text(table_header_all)

df = pd.DataFrame(columns=headers)
#table data 
for i in table_comp[0].find_all("tr")[1:]:
    table_row = i.find_all("td")
    print(table_row)
    length = len(df)
    print(length)
    text = [i.text for i in table_row]
    df.loc[length] = text
    

        
        
        