import requests
from bs4 import BeautifulSoup

def urlSpaces(str):
    return str.replace(" ", "-")

# Ask user for a keyword
keyword = urlSpaces(input("Enter a search keyword: "))
# Ask user for a location
place = urlSpaces(input("Where would like the job to be located?  "))
# Ask user for a title
title = input("What is the exact title of the position? ")

# Create URL with query paramaters
url = f"https://www.monster.com/jobs/search/?q={keyword}&where={place}"

print(url)

# HTTP request to URL returns the HTML data as an object
page = requests.get(url)

# parse the HTML content object into a Beautiful Soup object
soup = BeautifulSoup(page.content, "html.parser")

# find the div containing all the search results
results = soup.find(id='ResultsContainer')

# filtering results to get only the ones with the right title
# jobs_with_title = results.find_all('h2', 
#                                    string=lambda text: title in text.lower())

# returns an iterable 
# containing all the HTML for all the job listings
job_elems = results.find_all('section', class_='card-content')

# iterating over the listings to print each
for job_elem in job_elems:
    # Each job_elem is a new BeautifulSoup object.
    # You can use the same methods on it as you did before.
    title_elem = job_elem.find('h2', class_='title')
    company_elem = job_elem.find('div', class_='company')
    location_elem = job_elem.find('div', class_='location')
    # disregard problematic elements and skip over while parsing
    if None in (title_elem, company_elem, location_elem):
        continue
    # accessing the text inside the element, 
    # and stripping away white space
    print(title_elem.text.strip())
    print(company_elem.text.strip())
    print(location_elem.text.strip())
    print()

