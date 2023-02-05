# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import re

# create a variable to hold the url I want to scrape
url = 'https://webscraper.io/test-sites/e-commerce/allinone/phones/touch'
# check the request status, to ensure we can collect data
page = requests.get(url) 
# print(page) -- Response came back at 200

# create a variable that pulls the HTML doc
soup = BeautifulSoup(page.text, 'lxml')
# print(soup) -- HTML doc received 

# call the html tag with specific attributes
soup = soup.find('div', {'class':'container test-site'})
# print(soup) -- worked. it called all of the attributes from the HTML

# pull the price of an item and extract just the string
#soup = soup.find('h4', {'class':'pull-right price'})
# print(soup.string) -- pulled back just the price 

prices = soup.find_all('h4', class_ = 'pull-right price') 
# print(prices)

titles = soup.find_all('a', class_ = 'title')
# print(titles)

reviews = soup.find_all('p', class_ = 'pull-right')
# print(reviews)

twoAttrs = soup.find_all(['a', 'div'])
# print(twoAttrs)

# will search for all code that either have the attribute (id) (true) or code excluding that attr (false)
findClass = soup.find_all(id = True)

findString = soup.find_all(string = 'Iphone')
# print(findString)

findStringsWithRe = soup.find_all(string = re.compile('Iph'))
# print(findStringsWithRe)

pullPriceEff = soup.find_all(class_ = re.compile('pull'))
# print(pullPriceEff)

pullAttrEff = soup.find_all('p', class_ = re.compile('pull'))
print(pullAttrEff

      
      
      
      
      
      
      
      
      
      
      
      
      