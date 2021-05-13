# -*- coding: utf-8 -*-
"""
Created on Wed May 12 11:00:38 2021

@author: Amir Ostad
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('dark')
plt.style.use('seaborn')

def get_hist(df):
    
    """plot histograms for the numerical features
    arg:
        Dataframe df: dataframe of jobs
    """
    df.hist(bins=15)
    plt.show()

def get_boxplot(df, columns_list):
    
    """plot boxplots for the listed numerical features
    args:
        Dataframe df: dataframe of jobs
        list column_list: list of columns you want to be plotted
    """
    df.boxplot(column=columns_list)
    plt.show()
    
def get_correlation(df):
        
    """plot correlation heatmap for the numerical features
    arg:
        Dataframe df: dataframe of jobs
    """
    ax = plt.axes()
    sns.heatmap(df.corr(), annot=True, fmt='0.2f', ax=ax)
    ax.set_title('Correlation Heatmap')
    plt.show()
    
def get_countplot(df):
    
    """plot bar charts (count plots) for the categorical features
    arg:
        Dataframe df: dataframe of jobs
    """
    for col in df.select_dtypes(include=['object']).columns:
        ax = sns.countplot(x=col, data=df, 
                           order=df[col].value_counts().index)
        ax.set_xticklabels(ax.get_xticklabels(), rotation=90)
        plt.show()