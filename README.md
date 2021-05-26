# Web Scraping and Predicting Job Salaries
In this project, data scientist job openings will be web scraped and compared in terms of earnings.

## Publication
Here is the corresponding blog post which was published through GeekCulture publication: [data_science_salaries](https://amirostad.medium.com/use-data-science-to-predict-data-scientists-earnings-641849c7270)

## Motivation
1. Can a data scientist's salary be predicted and if so how accurately?
2. What features are important in predicting a data scientist's salary?
3. Another motivation was to see the relative number of data scientist jobs posted in different states in USA.
4. What industries/sectors pay higher salaries?

## Project overview
- The objective is to predict the salary of data scientist positions based on location, seniority, type of the company, industry, etc.
- The dataset used in this project is a combination of dataset obtained from https://www.kaggle.com/andrewmvd/data-scientist-jobs and extra data scientist positions scraped by  glassdoor scraper developed and uploaded to this repository
- Cleaned dataset of over 5500 data scientist positions
- Created and optimized Random Forest Regression model by using GridSearchCV to reach MAE=22.32, RMSE=28.61, and R<sup>2</sup>score=0.40
- Model was saved using joblib library

## Requirements
- Python 3.9
- Packages: pandas, numpy, sklearn, matplotlib, seaborn, joblib
- For more info, see requirements.txt file

## Data collection
- The dataset from kaggle was used in combination with over 1500 data scientist positions scraped with the glassdoor_scraper developed and uploaded in this repository. 
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
- Numerical variables: their distribution and correlations were checked as shown in the following images

![alt_text](https://github.com/amirostad/Web_scraping_jobs/blob/master/plots/1_histograms.png "histograms")

In the above plot, the distributions of numerical features and the response variable (Average_salary) are displayed.
It can be seen that the average salary distribution is nearly a normal distribution but skewed to the left. Also, the salary numbers are divided by 1000 and are in USD.

![alt_text](https://github.com/amirostad/Web_scraping_jobs/blob/master/plots/2_correlation_heatmap.png "correlation heatmap")


- Categorical variables: their value counts were checked as shown in the following images

![alt_text](https://github.com/amirostad/Web_scraping_jobs/blob/master/plots/3_jobtitles.png "job titles")

![alt_text](https://github.com/amirostad/Web_scraping_jobs/blob/master/plots/4_jobseniority.png "job seniority")

![alt_text](https://github.com/amirostad/Web_scraping_jobs/blob/master/plots/5_industry.png "industry")

![alt_text](https://github.com/amirostad/Web_scraping_jobs/blob/master/plots/6_sector.png "sector")

![alt_text](https://github.com/amirostad/Web_scraping_jobs/blob/master/plots/7_ownership.png "ownership")

![alt_text](https://github.com/amirostad/Web_scraping_jobs/blob/master/plots/8_size.png "size")

![alt_text](https://github.com/amirostad/Web_scraping_jobs/blob/master/plots/9_state.png "state")


## Modeling
I used one-hot encoding for the categorical features. Therefore, there was quite a bit of sparsity in the features matrix (lots of zeros). Considering the sparsity and its many other strengths, I utilized random forest regression.

Furthermore, corss validation with negative RMSE criterion was used to quickly check the effectiveness of the model.
Later, by using GridSearchCV, the parameters for the model were optimized and the final best fitted model was selected.

## Model performance
3 different metrics for the final best fitted model were calculated as follows:
- MAE = 22.32
- RMSE = 28.61
- R<sup>2</sup>score = 0.40

## Feature importance
The most importance features, i.e. features with the highest impact on the response variable, are shown below.
![alt_text](https://github.com/amirostad/Web_scraping_jobs/blob/master/plots/10_feature_importance.png "feature importance")

The top 20 features in the above plot are:
1. State_CA: this feature is equal to 1 if the position is located in California and 0 for other locations
2. State_NY: this feature is equal to 1 if the position is located in New York and 0 for other locations
3. Company_age: how old the company posting the position is
4. Rating: rating of the company on glassdoor
5. Employer_provided: this feature is equal to 1 if the salary data for the position is provided by the employer otherwise 0
6. Title_data scientist: this feature is equal to 1 if the position title contains "data scientist"
7. Sector_Information Technology: this feature is equal to 1 if the company operates in "Information Technology" sector
8. Seniority_senior: this feature is equal to 1 if the position is a senior level one
9. Title_other: this feature is equal to 1 if the position is in the data science field but the exact title is unknown
10. State_FL: this feature is equal to 1 if the position is located in Florida and 0 for other locations
11. State_IL: this feature is equal to 1 if the position is located in Illinois and 0 for other locations
12. Type of ownership_Company - Public: this feature is equal to 1 if the company is public
13. Title_data engineer: this feature is equal to 1 if the position title contains "data engineer"
14. Size_10000+ employees: this feature is equal to 1 if the company has more than 10,000 employees
15. State_OH: this feature is equal to 1 if the position is located in Ohio and 0 for other locations
16. Seniority_other: this feature is equal to 1 if the seniority level of the position is not explicitly mentioned either "senior" or "junior"
17. State_NJ: this feature is equal to 1 if the position is located in New Jersey and 0 for other locations
18. Type of ownership_Company - Private: this feature is equal to 1 if the company is private
19. State_MI: this feature is equal to 1 if the position is located in Michigan and 0 for other locations
20. Size_51 to 200 employees: this feature is equal to 1 if the company has 51–200 employees

## COMING SOON:
<span style="color:red">More models and production section (flask endpoint) will be added soon!</span>

## Acknowledgments
This project was inspired by https://github.com/PlayingNumbers/ds_salary_proj
