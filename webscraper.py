# Webscrape the title of the YouTube link
# https://www.youtube.com/watch?v=B83nmCSwRuw

import requests
from bs4 import BeautifulSoup

# link = input("please enter the YouTube URL:  ")
link = "https://www.youtube.com/watch?v=B83nmCSwRuw"

# after making an HTTP request `requests.get(link)`, the website will provide a response.
response = requests.get(link)

# BeautifulSoup is a Python library used for web scraping and data extraction from HTML and XML files
# BeautifulSoup() takes 1.the HTML content (response), and 2.the parser to use when parsing the HTML content.
# "html.parser" is a built-in parser in the BeautifulSoup library.
scrapings = BeautifulSoup(response.text, "html.parser")

# Extract the title
title_tag = scrapings.find("meta", attrs={"name": "title"})
title = title_tag["content"] if title_tag else ""

# Extract other data
req = input("please enter what you would like to read (e.g. title, description):  ")

# if the attribute is a "name" type (e.g. title)
if scrapings.find("meta", attrs={"name": req}) != None:
    data_tag = scrapings.find("meta", attrs={"name": req})
    data = data_tag["content"]

# if the attribute is described as "property"
elif scrapings.find("meta", attrs={"property": req}) != None:
    data_tag = scrapings.find("meta", attrs={"property": req})
    data = data_tag["content"]

# if the attribute is described as "itemprop"
elif scrapings.find("meta", attrs={"itemprop": req}) != None:
    data_tag = scrapings.find("meta", attrs={"itemprop": req})
    data = data_tag["content"]

else:
    data = "I have not learned how to check that yet"

print()
print("title :", title)

print()
print(req, ":", data)