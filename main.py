# -*- coding: utf-8 -*-
"""
Created on Tue May 11 11:50:19 2021

@author: Amir Ostad
"""

import data_cleaning as dc
import eda

df = dc.get_clean_dataframe()

eda.get_hist(df)
eda.get_boxplot(df, ['Average_salary', 'Min_salary', 'Max_salary'])
eda.get_correlation(df)
eda.get_countplot(df)