# -*- coding: utf-8 -*-
"""
Created on Wed May 12 14:55:52 2021

@author: Amir Ostad
"""
import features
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import GridSearchCV

def get_model(X):
    
    """Train and optimize model
    arg:
        Dataframe X: preprocessed dataframe of jobs
    
    return:
        regression model
        
    """
    
    rf = RandomForestRegressor(criterion='mse')

    # extracting the response variable
    y = X.pop("Average_salary")
    
    X = features.get_features(X)
    print(20 * "*" + " Getting features ended successfully!")
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,
                                                            random_state=23)
    
    cv = cross_val_score(rf,X_train,y_train,cv=10)
    print("cross validation scores:\n", cv)
    print("the average of the cross validation scores: ", cv.mean())
    
    
    param_grid =  {'n_estimators': [10, 25, 50, 100, 200, 400, 800, 1000],
                                      'bootstrap': [True],
                                      'max_depth': [2, 5, 10, 15, 20],
                                      'max_features': ['auto','sqrt',10],
                                      'min_samples_leaf': [2,3,4,5,6],
                                      'min_samples_split': [2,3,4]}
    
    
    # For a quick check
    # param_grid =  {'n_estimators': [50],
    #                                   'bootstrap': [True],
    #                                   'max_depth': [2],
    #                                   'max_features': ['auto','sqrt',10],
    #                                   'min_samples_leaf': [2,3],
    #                                   'min_samples_split': [2,3]}
    
    cv = GridSearchCV(rf, param_grid = param_grid, cv = 5, verbose = False,
                      n_jobs = -1)
    rfs = cv.fit(X_train,y_train)
    
    # picking the best of them
    rf = rfs.best_estimator_.fit(X_train,y_train)
    
    # y_train_hat = rf.predict(X_train)
    # y_test_hat = rf.predict(X_test)
    
    # save datasets
    X_train.to_csv('./data/X_train.csv', index=False)
    X_test.to_csv('./data/X_test.csv', index=False)
    y_train.to_csv('./data/y_train.csv', index=False)
    y_test.to_csv('./data/y_test.csv', index=False)
    
    # save model using joblib
    FILENAME = "rfr_saved_model.sav" # save random forest regressor 
    joblib.dump(rf, FILENAME)
    
    return rf
    
