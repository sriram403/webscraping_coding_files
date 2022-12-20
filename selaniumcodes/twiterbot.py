from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
import time 
from bs4 import BeautifulSoup

chrome_s = webdriver.Chrome("C:/chromedriver.exe")
chrome_s.get("https://twitter.com/i/flow/login")

time.sleep(4)
name_b = chrome_s.find_element("xpath",'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
name = name_b.send_keys("justlookingelon")

chrome_s.find_element("xpath",'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]').click()
time.sleep(4)
password_b = chrome_s.find_element("xpath",'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
password = password_b.send_keys("adithiya505password")

chrome_s.find_element("xpath",'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div').click()

WebDriverWait(chrome_s,10).until(ec.presence_of_element_located((By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div/label/div[2]/div/input')))

search_b = chrome_s.find_element("xpath",'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div/label/div[2]/div/input')
search_b.send_keys("Robert Downey Jr")
search_b.send_keys(Keys.ENTER)
time.sleep(2)
chrome_s.find_element("xpath",'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[1]/div[1]/div[2]/nav/div/div[2]/div/div[3]/a/div/div/span').click()
time.sleep(2)
chrome_s.find_element('xpath','//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/section/div/div/div[1]/div/div/div/div/div[2]/div[1]/div[1]/div/div[1]/a/div/div[1]/span/span').click()
time.sleep(5)
soup = BeautifulSoup(chrome_s.page_source,"lxml")
#all_tweets = soup.find_all("div",class_="css-901oao r-18jsvk2 r-37j5jr r-a023e6 r-16dba41 r-rjixqe r-bcqeeo r-bnwqim r-qvutc0")
all_tweets =soup.find_all("div",{"data-testid":"tweetText"})
len(all_tweets)
print("starting to collect tweets from elon musk...")
tweets = []
while True:
    for word in all_tweets:
        t = word.text
        tweets.append(t)
    chrome_s.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    tweets_2 = list(set(tweets))
    time.sleep(5)
    soup =BeautifulSoup(chrome_s.page_source,"lxml")
    all_tweets = soup.find_all("div",{"data-testid":"cellInnerDiv"})
    if len(tweets_2)>=200:
        break
len(tweets_2)
print("finished...")