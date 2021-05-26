# -*- coding: utf-8 -*-
"""
Created on Tue May 11 21:00:07 2021

@author: Amir Ostad 
"""
# import glassdoor_scraper as gs
import pandas as pd

def get_clean_dataframe(num_jobs=100):
    """
    Gets raw dataframe directly from glassdoor_scraper.py or from a csv file.
    Cleans the raw dataframe.
    
    args:
        int num_jobs: number of desirable jobs passed to the scraper
    
    return:
        Dataframe df: cleaned dataframe
    """
    
    # df = gs.get_jobs(num_jobs=num_jobs)
    
    df = pd.read_csv('./data/df.csv')
    
    #%% Salary
    
    # Remove instances without salary estimates
    df = df[df['Salary Estimate'] != '-1']
    
    ## Remove K and $ 
    df['Salary Estimate'] = df['Salary Estimate'].apply(lambda x: x.replace('K', '').replace('$', ''))
    
    ## Add hourly and employer provided binary columns
    df['Hourly'] = df['Salary Estimate'].apply(lambda x: 1 if 'per hour' in x.lower() else 0)
    df['Employer_provided'] = df['Salary Estimate'].apply(lambda x: 1 if 'employer est' in x.lower() else 0)
    
    ## Add min, max, and average salary columns and cast them into integer type
    df['Min_salary'] = df['Salary Estimate'].apply(lambda x: int(x.split('-')[0]))
    # df['Max_salary'] = df['Salary Estimate'].apply(lambda x: int(x.split('$')[1]))
    df['Max_salary'] = df['Salary Estimate'].apply(lambda x: x.split('-')[1]).replace('[^0-9]', '', regex=True)
    df['Max_salary'] = df['Max_salary'].apply(int)
    
    ### Convert hourly wages to annual
    df['Min_salary'] = df.apply(lambda x: x.Min_salary if x.Hourly == 0 else x.Min_salary*2.05, axis=1)
    df['Max_salary'] = df.apply(lambda x: x.Max_salary if x.Hourly == 0 else x.Max_salary*2.05, axis=1)
    
    df['Average_salary'] = (df.Min_salary + df.Max_salary)/2
    
    ## Remove the initial salary estimate column
    df.drop('Salary Estimate', axis=1, inplace=True)
    
    #%% Rating
    
    ## Ensure ratings are float type
    df['Rating'] = df['Rating'].apply(lambda x: float(x))
    
    #%% Company name
    
    ## Remove rating from the end of company names
    df['Company Name'] = df['Company Name'].apply(lambda x: x.split('\n')[0])
    
    #%% State: what state is the job in
    
    df['State'] = df['Location'].apply(lambda x: x.split()[-1])
    df = df[df.State != 'Kingdom'] # remove United Kingdom
    df = df[df.State != 'States'] # remove United States
    #%% Company age
    
    # Replace non-numeric cells in Founded column with -1
    df['Founded'].replace('[^0-9]', -1, regex=True, inplace=True)
    
    df['Company_age'] = df['Founded'].apply(lambda x: 2021-int(x) if int(x)>0 else -1)
    
    
    #%% Organize job titles
    
    def title_organizer(x):
        x = x.lower()
        if ('data scientist' in x) or ('data science' in x) :
            return 'data scientist'
        elif 'data engineer' in x:
            return 'data engineer'
        elif 'deep learning' in x:
            return 'deep learning engineer'
        elif 'machine learning' in x:
            return 'machine learning engineer'
        elif 'director' in x:
            return 'director'
        elif 'manager' in x:
            return 'manager'
        elif 'analyst' in x:
            return 'analyst'
        elif 'researcher' in x:
            return 'researcher'
        else:
            return 'other'
    df['Title'] = df['Job Title'].apply(title_organizer)
    
    #%% Senior position?
    
    def senior_junior(x):
        x = x.lower()
        if 'sr' in x or 'senior' in x or 'sr.' in x or 'lead' in x or 'principal' in x or 'vp' in x or 'manager' in x:
            return 'senior'
        elif 'jr' in x or 'junior' in x or 'jr.' in x:
            return 'junior'
        else:
            return 'other'
    df['Seniority'] = df['Job Title'].apply(senior_junior)        
    
    #%% Size
    
    df['Size'].replace('Unknown', '-1', regex=True, inplace=True)
    df['Size'] = df['Size'].str.lower()
    
    #%% Type of ownership
    
    df['Type of ownership'].replace('Unknown', '-1', regex=True, inplace=True)
    
    #%% Drop unwanted columns, reorder the remining columns, and write the dataframe to csv format
    
    # Max_salary and Min_salary are dropped too because we calculated the
    # response variable, Average_salary, by using them.
    df.drop(['Company Name', 'Location', 'Founded', 'Job Title', 
             'Revenue', 'Min_salary', 'Max_salary'], inplace=True,
            axis=1)
    
    df = df.reindex(columns=['Average_salary', 'Title','Seniority', 
                             'Rating', 'Hourly', 'Employer_provided', 
                             'Company_age', 
                             'Industry', 'Sector', 'Type of ownership',
                             'Size', 'State'])
    
    df.to_csv('./data/df_cleaned.csv', index=False)
    
    return df
    
