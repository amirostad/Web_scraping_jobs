# Web Scraping and Predicting Job Salaries
In this project, data scientist job openings will be web scraped and compared in terms of earnings.

## Motivation
1. Can a data scientist role's earnings be estimated?
2. What features are important in predicting a data scientist's earnings?

## Project Overview
- The objective is to predict the salary of data scientist positions based on location, seniority, type of the company, industry, etc.
- The dataset used in this project is a combination of dataset here https://www.kaggle.com/andrewmvd/data-scientist-jobs and extra data scientist positions scraped by glassdoor scraper uploaded to this repository
- Cleaned dataset of about 4000 data scientist positions
- Created and optimized Random Forest Regression model by using GridSearchCV to reach MAE=0.04, RMSE=0.18, and $R^2$ score=0.99

## Acknowledgments
This project was inspired by https://github.com/PlayingNumbers/ds_salary_proj
