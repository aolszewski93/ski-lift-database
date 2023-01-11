"""
This is an example from real python that exercises webscraping for data collection.
link: https://realpython.com/beautiful-soup-web-scraper-python/
"""

import requests

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

print(page.text)
