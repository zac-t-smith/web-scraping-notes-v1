# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
# confirm imports are working before moving forward

# creating a variable to hold the url we will be scraping
url = 'https://webscraper.io/test-sites/e-commerce/allinone/computers'
page = requests.get(url)
# confirm the vairable page has a response code of 200 before moving forward

# create a variable that starts parsing the url with BeautifulSoup
soup = BeautifulSoup(page.text, 'lxml')
# print the parsing variable to confirm the HTML is callected to the console

# making a variable to call a tag from the HTML and make it a string
tag = soup.header.p.string

# pulling header, tags, and an attribute 
tag = soup.header.a
tag = tag.attrs
# print(tag) above to see results

# target a specific attribute and add a new one into the HTML
tag['data-target'] = 'this is a new attribute'
print(tag)