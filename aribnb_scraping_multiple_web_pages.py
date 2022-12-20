import requests 
import pandas as pd
from bs4 import BeautifulSoup
url = "https://www.airbnb.co.in/s/United-States/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_lengths%5B%5D=one_week&price_filter_input_type=0&price_filter_num_nights=5&place_id=ChIJCzYy5IS16lQRQrfeQ5K5Oxw&date_picker_type=calendar&checkin=2022-11-11&checkout=2022-11-12&source=structured_search_input_header&search_type=filter_change"
page = requests.get(url)

soup = BeautifulSoup(page.text,"lxml")

columns_all = soup.find_all("div",class_="gh7uyir giajdwt g14v8520 dir dir-ltr")

div_all = columns_all[0].find_all("div",class_="c4mnd7m dir dir-ltr")

#a = div_all[1].find("a",class_="ln2bl2p dir dir-ltr")
#div_all[1].find("span",class_="r1dxllyb dir dir-ltr").text

df = pd.DataFrame({"Links":[''],"Title":[''],"Details":[''],"Ratings":[''],"Beds":[''],"Rate":['']}) 
while True:
    for post in div_all:
        try:
            link_half = post.find("a",class_="ln2bl2p dir dir-ltr").get("href")
            link_half
            added_link = "https://www.airbnb.co.in"+link_half
            title = post.find("div",class_="t1jojoys dir dir-ltr").text
            description = post.find("span",class_="t6mzqp7 dir dir-ltr").text
            beds = post.find("span",class_="dir dir-ltr").text
            #reviews = post.find("span",class_="r1dxllyb dir dir-ltr").text
            reviews = div_all[1].find("span",class_="r1dxllyb dir dir-ltr").text
            rate = post.find("span",class_="a8jt5op dir dir-ltr").text
            df = pd.concat([df,pd.DataFrame({df.columns[0]:[added_link],df.columns[1]:[title],df.columns[2]:[description],df.columns[3]:[reviews],df.columns[4]:[beds],df.columns[5]:[rate]})],ignore_index=True)
        except:
            pass
    link = soup.find("a",{"aria-label":"Next"}).get("href")
    link
    added_new_link = "https://www.airbnb.co.in"+link
    added_new_link
    page = requests.get(added_new_link)

    soup = BeautifulSoup(page.text,"lxml")

    columns_all = soup.find_all("div",class_="gh7uyir giajdwt g14v8520 dir dir-ltr")

    div_all = columns_all[0].find_all("div",class_="c4mnd7m dir dir-ltr")
df.to_csv("A:/Courses/Web_S_ing_in_Python_With_BeautifulSoup_and_Selenium/webscraping_coding_files/data's/airbnb.csv",index=False)