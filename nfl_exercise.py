# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 15:47:00 2022

@author: sriram
"""

import requests,pandas as pd
from bs4 import BeautifulSoup
url = "https://www.nfl.com/standings/league/2022/REG"
page = requests.get(url)
soup = BeautifulSoup(page.text,"lxml")
soup

#getting all table content
all_table = soup.find_all("div",class_="d3-o-table--horizontal-scroll")[0]
all_table

#getting header name 
table_header_all = all_table.find_all("thead")[0]
table_header_all
header = []
for i in table_header_all.find_all("th"):
    header.append(i.text)
header

#creating dataframe 
df = pd.DataFrame(columns=header)
len(df)

#getting all the table row parent html tags
table_row_all = soup.find("section",class_="d3-l-grid--outer d3-l-section-row nfl-o-standings")
table_row_all

#getting table_body tags
first_name = table_row_all.find("tbody")
first_name

#getting all the tabel row information
rows_data = first_name.find_all("tr")[::-1]#reversing our content 
len(rows_data)

#adding values to our dataframe
for index,i in enumerate(rows_data):
    rows_scope = i.find_all("td",{"scope":True})#getting only the scope attrs values
    
    name = rows_scope[0].find("div",class_="d3-o-club-shortname").text#our scope attrs 
    #contain the required name for our data 
    
    #adding other data to our data frame
    length = len(df)#length of the dataframe
    
    text = [j.text for j in rows_data[index].find_all("td",{"scope":False})]#getting other
    #values without scope attrs which contains our normal data values
    
    text.insert(0,name)#inserting our name into our normal datavalues

    df.loc[length] = text #adding the values finaly to our dataframe with respective index
    #[0,1,2,....]
    

df.to_csv("A:/Courses/Web_S_ing_in_Python_With_BeautifulSoup_and_Selenium/webscraping_coding_files/data's/nfl.csv")        



