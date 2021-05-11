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
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
import time
import pandas as pd
import snoop

# DRIVER_PATH = 'chromedriver'
# options = Options()
# options.headless = False # With (FALSE) or without (TRUE) user interface
# options.add_argument("--window-size=1200,675")

# PATIENCE_TIME = 60

# driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
# job_to_lookfor = 'Data%20Scientist'
# url = "https://www.glassdoor.com/Job/jobs.htm?sc.keyword=" + job_to_lookfor + "&suggestCount=0&suggestChosen=false&clickSource=searchBox&locId=1&locT=N&locName=United%20States"
# driver.get(url)

# page_number = 1 # Currently on page 1
# while (page_number <= 5):
    
#     # Test for the "Sign Up" prompt and get rid of it.
#     try:
#         driver.find_element_by_css_selector('[alt="Close"]').click() # Clicking to the X.
#         print(' x out worked')
#     except NoSuchElementException:
#         print(' x out failed')
#         pass
    
#     # Go page after page and scrape jobs
#     try:
#         print('currently on page {}'.format(page_number))
#         nextPageButton = driver.find_element_by_xpath('.//li[@class="css-1yshuyv e1gri00l3"]//a')
#         time.sleep(2)
#         nextPageButton.click()
#         page_number += 1
#         print('going to page {}'.format(page_number))
#         time.sleep(5)
#     except Exception as e:
#         print(e)
#         break
# print("********** Next page process complete! **********")
# time.sleep(10)

##############################################################################
@snoop # snoop shows the line of a function being executed
def get_jobs(job_to_lookfor='Data%20Scientist', num_jobs=1000, verbose=True, DRIVER_PATH = 'chromedriver', slp_time=15):
    
    '''Gathers jobs as a dataframe, scraped from Glassdoor'''
    
    options = Options()
    options.headless = False # With (FALSE) or without (TRUE) user interface
    options.add_argument("--window-size=1200,675")
    
    PATIENCE_TIME = 60
    
    driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
    
    url = "https://www.glassdoor.com/Job/jobs.htm?sc.keyword=" + job_to_lookfor + "&suggestCount=0&suggestChosen=false&clickSource=searchBox&locId=1&locT=N&locName=United%20States"
    driver.get(url)
    jobs = []

    while len(jobs) < num_jobs:  #If true, should be still looking for new jobs.

        #Let the page load. Change this number based on your internet speed.
        #Or, wait until the webpage is loaded, instead of hardcoding it.
        time.sleep(slp_time)

        try:
            driver.find_element_by_css_selector('[alt="Close"]').click() #clicking to the X.
            print(' x out worked')
        except NoSuchElementException:
            print(' x out failed')
            pass

        
        # Going through each job in this page
        job_buttons = driver.find_elements_by_xpath("//ul//li//div//div//a//span")   # Job Listing. These are the buttons we're going to click.
        # print("job_buttons length: ".format(len(job_buttons)))
        for job_button in job_buttons:  

            print("Progress: {}".format("" + str(len(jobs)) + "/" + str(num_jobs)))
            if len(jobs) >= num_jobs:
                break

            job_button.click()  # You might 
            time.sleep(1)
            collected_successfully = False
            
            while not collected_successfully:
                try:
                    company_name = driver.find_element_by_xpath('//*[@id="JDCol"]/div/article/div/div[1]/div/div/div[1]/div[3]/div[1]/div[1]').text
                    location = driver.find_element_by_xpath('//*[@id="JDCol"]/div/article/div/div[1]/div/div/div[1]/div[3]/div[1]/div[3]').text
                    job_title = driver.find_element_by_xpath('.//*[@id="JDCol"]/div/article/div/div[1]/div/div/div[1]/div[3]/div[1]/div[2]').text
                    collected_successfully = True
                except:
                    time.sleep(5)

            try:
                salary_estimate = driver.find_element_by_xpath('.//span[@class="gray salary"]').text
            except NoSuchElementException:
                salary_estimate = -1 # You need to set a "not found value. It's important."
            
            try:
                rating = driver.find_element_by_xpath('.//span[@class="rating"]').text
            except NoSuchElementException:
                rating = -1 #You need to set a "not found value. It's important."

            #Printing for debugging
            if verbose:
                print("Job Title: {}".format(job_title))
                print("Salary Estimate: {}".format(salary_estimate))
                print("Job Description: {}".format(job_description[:500]))
                print("Rating: {}".format(rating))
                print("Company Name: {}".format(company_name))
                print("Location: {}".format(location))

            #Going to the Company tab...
            #clicking on this:
            #<div class="tab" data-tab-type="overview"><span>Company</span></div>
            try:
                driver.find_element_by_xpath('.//div[@class="tab" and @data-tab-type="overview"]').click()

                try:
                    #<div class="infoEntity">
                    #    <label>Headquarters</label>
                    #    <span class="value">San Francisco, CA</span>
                    #</div>
                    headquarters = driver.find_element_by_xpath('.//div[@class="infoEntity"]//label[text()="Headquarters"]//following-sibling::*').text
                except NoSuchElementException:
                    headquarters = -1

                try:
                    size = driver.find_element_by_xpath('.//div[@class="infoEntity"]//label[text()="Size"]//following-sibling::*').text
                except NoSuchElementException:
                    size = -1

                try:
                    founded = driver.find_element_by_xpath('.//div[@class="infoEntity"]//label[text()="Founded"]//following-sibling::*').text
                except NoSuchElementException:
                    founded = -1

                try:
                    type_of_ownership = driver.find_element_by_xpath('.//div[@class="infoEntity"]//label[text()="Type"]//following-sibling::*').text
                except NoSuchElementException:
                    type_of_ownership = -1

                try:
                    industry = driver.find_element_by_xpath('.//div[@class="infoEntity"]//label[text()="Industry"]//following-sibling::*').text
                except NoSuchElementException:
                    industry = -1

                try:
                    sector = driver.find_element_by_xpath('.//div[@class="infoEntity"]//label[text()="Sector"]//following-sibling::*').text
                except NoSuchElementException:
                    sector = -1

                try:
                    revenue = driver.find_element_by_xpath('.//div[@class="infoEntity"]//label[text()="Revenue"]//following-sibling::*').text
                except NoSuchElementException:
                    revenue = -1

                try:
                    competitors = driver.find_element_by_xpath('.//div[@class="infoEntity"]//label[text()="Competitors"]//following-sibling::*').text
                except NoSuchElementException:
                    competitors = -1

            except NoSuchElementException:  #Rarely, some job postings do not have the "Company" tab.
                headquarters = -1
                size = -1
                founded = -1
                type_of_ownership = -1
                industry = -1
                sector = -1
                revenue = -1
                competitors = -1

                
            if verbose:
                print("Headquarters: {}".format(headquarters))
                print("Size: {}".format(size))
                print("Founded: {}".format(founded))
                print("Type of Ownership: {}".format(type_of_ownership))
                print("Industry: {}".format(industry))
                print("Sector: {}".format(sector))
                print("Revenue: {}".format(revenue))
                print("Competitors: {}".format(competitors))
                print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

            jobs.append({"Job Title" : job_title,
            "Salary Estimate" : salary_estimate,
            "Job Description" : job_description,
            "Rating" : rating,
            "Company Name" : company_name,
            "Location" : location,
            "Headquarters" : headquarters,
            "Size" : size,
            "Founded" : founded,
            "Type of ownership" : type_of_ownership,
            "Industry" : industry,
            "Sector" : sector,
            "Revenue" : revenue,
            "Competitors" : competitors})
            #add job to jobs
            
            
        #Clicking on the "next page" button
        try:
            driver.find_element_by_xpath('.//li[@class="css-1yshuyv e1gri00l3"]//a').click()
        except NoSuchElementException:
            print("Scraping terminated before reaching target number of jobs. Needed {}, got {}.".format(num_jobs, len(jobs)))
            break

    return pd.DataFrame(jobs)  #This line converts the dictionary object into a pandas DataFrame.
