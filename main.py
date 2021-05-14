# -*- coding: utf-8 -*-
"""
Created on Tue May 11 11:50:19 2021

@author: Amir Ostad
"""

import data_cleaning as dc
import eda
import joblib
import model
import pandas as pd
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

#%% Get the clean data
df = dc.get_clean_dataframe()

#%% EDA: Visualize the data
eda.get_hist(df)
eda.get_boxplot(df, ['Average_salary', 'Min_salary', 'Max_salary'])
eda.get_correlation(df)
eda.get_countplot(df)

#%% Modeling
try:
    # load the model form disk
    rfr_loaded_model = joblib.load("rfr_saved_model.sav")
    
except:
    rfr_loaded_model = model.get_model(df)
    
print("The optimized Random Forest Regressor model: \n", rfr_loaded_model)
print("The number of features used to fit the Random Forest Regressor model: {}". format(rfr_loaded_model.n_features_))    

#%% Model's accuracy
X_test = pd.read_csv('./data/X_test.csv')
y_test = pd.read_csv('./data/y_test.csv')
y_pred = rfr_loaded_model.predict(X_test)    

# Which features are more important
feat_importances = pd.Series(rfr_loaded_model.feature_importances_,
                                 index=X_test.columns)
feat_importances.nlargest(20).plot(kind='barh', color='teal')
print(feat_importances.sort_values())
print("Random forest regressor's mean absolute error (MAE) = ", mean_absolute_error(y_test, y_pred))
print("Random forest regressor's roor mean squared error (RMSE) = ", pow(mean_squared_error(y_test, y_pred), 0.5))
print("Random forest regressor's R2 score = ", r2_score(y_test, y_pred))
