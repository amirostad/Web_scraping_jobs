# -*- coding: utf-8 -*-
"""
Created on Wed May 12 15:06:54 2021

@author: Amir Ostad
"""

import pandas as pd

def get_features(X):
    """
    Fills in the null values for numerical values.
    Creates dummies for categorical variables.
    Produces the final feature matrix, X.
    Returns X.
    """
    print(20 * "*" + " data cleaning initiated!")
    
    # separating numerical and categorical features into two dataframes
    num_X = X.select_dtypes(include=['int', 'float', 'int64', 'float64'])
    cat_X = X.select_dtypes(include=['object'])

    # filling null values of numerical features with their means
    for col in num_X.columns:
        X[col] = X[col].fillna(X[col].mean())

    # creating dummies for categorical variables and producing final X matrix
    for col in cat_X.columns:
        X = pd.concat([X.drop(col, axis=1),
                       pd.get_dummies(X[col], prefix=col, prefix_sep='_',
                                      drop_first=True)], axis=1)
    return X