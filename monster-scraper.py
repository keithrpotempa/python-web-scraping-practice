import requests
from bs4 import BeautifulSoup

def urlSpaces(str):
  str.replace(" ", "-")

keyword = urlSpaces(input("Enter a search keyword: "))
place = urlSpaces(input("Where would like the job to be located?  "))

url = f"https://www.monster.com/jobs/search/?q={keyword}&where={place}"
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id='ResultsContainer')

print(results.prettify())