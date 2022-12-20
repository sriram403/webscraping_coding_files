from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
import time 


driver = webdriver.Chrome("C:/chromedriver.exe")
driver.get("https://www.google.com")
bar = driver.find_element("xpath","/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
bar.send_keys("top 100 movies of all time")
bar.send_keys(Keys.ENTER)
driver.find_element("xpath",'//*[@id="rso"]/div[2]/div/div/div[1]/div/div/div[1]/div/a').click()
wait_to_confirm = WebDriverWait(driver,10).until(ec.presence_of_element_located((By.XPATH,'//*[@id="main"]/div/div[4]/div[3]/div[50]/div[1]/a/img')))
print("getting the picture")
time.sleep(5)
driver.execute_script("window.scrollTo(0,22710)")
path = "A:/Courses/Web_S_ing_in_Python_With_BeautifulSoup_and_Selenium/webscraping_coding_files/data's/jaw.png"
driver.find_element("xpath",'//*[@id="main"]/div/div[4]/div[3]/div[50]/div[1]/a/img').screenshot(path)
driver.save_screenshot("A:/Courses/Web_S_ing_in_Python_With_BeautifulSoup_and_Selenium/webscraping_coding_files/data's/jawpage.png")

