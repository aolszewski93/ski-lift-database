"""
This is an example from real python that exercises webscraping for data collection.
link: https://realpython.com/beautiful-soup-web-scraper-python/
"""

import requests
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

#prints the html to command line similar to inspect
# print(page.text)

#create a beautifulsoup object with the page content and choose the appropriate parser
soup = BeautifulSoup(page.content, "html.parser")

# grabs container for job postings
results = soup.find(id="ResultsContainer")

# create an iterable containing all of the html for all of the job postings. 
job_elements = results.find_all("div", class_="card-content")

for job_element in job_elements:
    print(job_element, end="\n"*2)
