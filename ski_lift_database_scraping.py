import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL = "https://liftblog.com/united-states/"
# page = requests.get(URL)
#
# #create a beautifulsoup object with the page content and choose the appropriate parser
# soup = BeautifulSoup(page.content, "html.parser")
#
# # grabs container for job postings
# results = soup.find(id="post-1491")
#
# #there are two lists on this page.  first is the states and second is sharing links
# states = results.find_all("ul")[0].find_all("a")
#
#
# for state in states:
#     state_name = state.text.strip()
#     state_link = state['href']
#     print(state_name)
#     print(state_link)

URL = "https://liftblog.com/alabama/"
page = requests.get(URL)

#create a beautifulsoup object with the page content and choose the appropriate parser
soup = BeautifulSoup(page.content, "html.parser")

# grabs container for job postings
results = soup.find("div", class_="entry-content")

ski_resorts = results.find_all("li")[0]

print(ski_resorts)
