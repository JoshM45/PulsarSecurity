#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup
URL = "https://www.pulsarsecurity.com/team"
page = requests.get(URL)

print(page.text)
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="block-team")

print(results.prettify())
name_elements = results.find_all("h3", class_="block-team-name")

# Get a list of full names

for name_element in name_elements:
    print(name_element.text)
    

# Get a list of first names
for name_element in name_elements:
    x = name_element.text.split()
    print(x[0])

    
# Get a list of last names

for name_element in name_elements:
    x = name_element.text.split()
    print(x[1])

