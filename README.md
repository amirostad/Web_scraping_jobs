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



## Acknowledgments
This project was inspired by https://github.com/PlayingNumbers/ds_salary_proj
