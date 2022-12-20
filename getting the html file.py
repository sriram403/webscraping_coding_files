from bs4 import BeautifulSoup
import requests

url = 'https://webscraper.io/test-sites/e-commerce/allinone/computers'

page = requests.get(url) #gives me value of whether a page can be accessible by python
#[200] yes [400] or anyother means no

soup = BeautifulSoup(page.text,"lxml")#getting the page html as text and changing them 
#back to html with the help of parser('lxml')


text_from_paragraph = soup.header.p.string #getting the page header,paragraph
#and its string value all at the same time 
#print(text_from_paragraph)

tag = soup.header.a
#print(tag.attrs)
print(tag["data-toggle"])