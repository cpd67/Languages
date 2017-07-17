#!/bin/python3

# https://www.dataquest.io/blog/web-scraping-tutorial-python/

# Use the requests library to download the page for scraping.
import requests

# Use the BeautifulSoup class from the bs4 library to parse the webpage document.
from bs4 import BeautifulSoup

webpage = requests.get("http://dataquestio.github.io/web-scraping-pages/ids_and_classes.html")

print(str(webpage.status_code))

print(webpage.content)

# Create a BeautifulSoup instance using the webpage content
soup = BeautifulSoup(webpage.content, 'html.parser')

# Pretty print the HTML content
print(soup.prettify())

# Can use soup.find() to find an element in the page
# soup.find_all() to find all instances of the element that you are looking for
# Pass the class_="<class-name>" or id="<id-name>" parameter to find_all() to get an element with a
# specific id or class name
# Use select() to use CSS selectors 
