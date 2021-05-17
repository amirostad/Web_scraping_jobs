# Web Scraping and Predicting Job Salaries
In this project, data scientist job openings will be web scraped and compared in terms of earnings.

## Motivation
1. Can a data scientist role's earnings be estimated?
2. What features are important in predicting a data scientist's earnings?

## Project overview
- The objective is to predict the salary of data scientist positions based on location, seniority, type of the company, industry, etc.
- The dataset used in this project is a combination of dataset obtained from https://www.kaggle.com/andrewmvd/data-scientist-jobs and extra data scientist positions scraped by glassdoor scraper uploaded to this repository
- Cleaned dataset of over 5500 data scientist positions
- Created and optimized Random Forest Regression model by using GridSearchCV to reach MAE=0.29, RMSE=2.26, and R<sup>2</sup>score=0.99
- Model was saved using joblib library

## Requirements
- Python 3.9
- Packages: pandas, numpy, sklearn, matplotlib, seaborn, joblib
- For more info, see requirements.txt file

## Data collection
- The dataset from kaggle was used in combination with over 1500 data scientist positions scraped with the glassdoor_scraper in this repository. 
- The glassdoor scraper in https://github.com/PlayingNumbers/ds_salary_proj was used as a base scraper but it had many broken HTML tags and defective Xpaths so a good portion of the Selenium code had to be revised.
- The following features were scraped for each position:
    - Salary Estimate
    - Rating
    - Company name
    - Location
    - Size of the company
    - Year the company was founded
    - Type of ownership
    - Industry
    - Sector
    - Revenue

## Data cleaning
- Parsed the salary estimates out of the raw data
- Created "Hourly" and "Employer_provided" columns to distinguish if a salary estimate was based on hourly rates and provided by the employer, respectively
- Created minimum and maximum salary columns for the positions and parsed the corresponding values out of the raw dat
- Created average salary column
- Cleaned the company name column by removing the ratings
- Extracted the state where each position is located. Created a state column
- Created founded column which contains the year each company was founded
- Using the founded column, the company age column was created
- Seniority column was created to show if a position was a senior role
- Title column was created to show the different categories for the posted roles such as data engineer, deep learning, analyst, ...
- For all the column if the corresponding value was not available, -1 was assigned for the particular position

## EDA
- Numerical variables: their distribution and correlations were checked
https://github.com/amirostad/Web_scraping_jobs/blob/master/plots/1_histograms.png

- Categorical variables: their value counts were checked


## Acknowledgments
This project was inspired by https://github.com/PlayingNumbers/ds_salary_proj
