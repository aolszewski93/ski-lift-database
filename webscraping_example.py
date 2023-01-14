"""
This is an example from real python that exercises webscraping for data collection.
link: https://realpython.com/beautiful-soup-web-scraper-python/
"""

import requests
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)


#define function that take beautiful soup object and prints out job data
def print_jobs(job_elements):
    for job_element in job_elements:
        title_element = job_element.find("h2", class_="title")
        company_element = job_element.find("h3", class_="company")
        location_element = job_element.find("p", class_="location")
        print("Job Title: " + title_element.text.strip())
        print("Company Name: " + company_element.text.strip())
        print("Location: " + location_element.text.strip())

        #find the link for the jobs
        links = job_element.find_all("a")
        #the second link is the one associated with the job application
        link = links[1]
        link_url = link["href"]
        print(f"Apply here: {link_url}\n")

#prints the html to command line similar to inspect
# print(page.text)

#create a beautifulsoup object with the page content and choose the appropriate parser
soup = BeautifulSoup(page.content, "html.parser")

# grabs container for job postings
results = soup.find(id="ResultsContainer")

# create an iterable containing all of the html for all of the job postings.
job_elements = results.find_all("div", class_="card-content")

# print_jobs(job_elements)

#find jobs that contain python in the title_element
python_jobs = results.find_all(
    "h2", string=lambda text: "python" in text.lower()
    )

python_job_elements = [
    h2_element.parent.parent.parent for h2_element in python_jobs
]

print_jobs(python_job_elements)
