# https://thinkdiff.net/python/python-selenium-webdriver-tutorial-how-to-scrap-data-from-javascript-based-website/

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
import time
import sys

# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

url = 'https://www.brainyquote.com/'
firefox_driver_path = '/usr/bin/geckodriver'

# create an instance of Options class
firefox_options = Options()
firefox_options.headless = True

# cap = DesiredCapabilities().FIREFOX
# cap["marionette"] = False

# make it headless
# firefox_options.add_argument('--headless')

# create an instance of webdriver.Firefox class
# (this will be our web browser)
webdriver = webdriver.Firefox(
  # firefox_binary=binary,
  # capabilities=cap,
  executable_path=firefox_driver_path, 
  options=firefox_options
)

# If from the terminal we pass any keyword, 
# the search_query will be replaced by that, 
# otherwise the default search query word will be “life”.

# default search query
search_query = "life"

if (len(sys.argv) >= 2):
  search_query = sys.argv[1]
  print(search_query)
  
# load the website, 
# automate the behavior 
# scrape the data 
# print in the terminal.

with webdriver as driver:
    # Set timeout time 
    wait = WebDriverWait(driver, 10)

    # retrive url in headless browser
    driver.get(url)
    
    # find search box
    search = driver.find_element_by_id("hmSearch")
    search.send_keys(search_query + Keys.RETURN)
    
    wait.until(presence_of_element_located((By.ID, "quotesList")))
    # time.sleep(3)
    results = driver.find_elements_by_class_name('m-brick')

    for quote in results:
      quoteArr = quote.text.split('\n')
      print(quoteArr)
      print()

    # must close the driver after task finished
    driver.close()