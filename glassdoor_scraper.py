# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 20:18:20 2021

@author: Amir Ostad
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

DRIVER_PATH = 'chromedriver'
options = Options()
options.headless = False # With (FALSE) or without (TRUE) user interface
options.add_argument("--window-size=1200,675")

PATIENCE_TIME = 60

driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
job_to_lookfor = 'Data%20Scientist'
url = "https://www.glassdoor.com/Job/jobs.htm?sc.keyword=" + job_to_lookfor + "&suggestCount=0&suggestChosen=false&clickSource=searchBox&locId=1&locT=N&locName=United%20States"
driver.get(url)

page_number = 1 # Currently on page 1
while (page_number <= 5):
    
    # Test for the "Sign Up" prompt and get rid of it.
    try:
        driver.find_element_by_css_selector('[alt="Close"]').click() # Clicking to the X.
        print(' x out worked')
    except NoSuchElementException:
        print(' x out failed')
        pass
    
    # Go page after page and scrape jobs
    try:
        print('currently on page {}'.format(page_number))
        nextPageButton = driver.find_element_by_xpath('.//li[@class="css-1yshuyv e1gri00l3"]//a')
        time.sleep(2)
        nextPageButton.click()
        page_number += 1
        print('going to page {}'.format(page_number))
        time.sleep(5)
    except Exception as e:
        print(e)
        break
print("********** Next page process complete! **********")
time.sleep(10)