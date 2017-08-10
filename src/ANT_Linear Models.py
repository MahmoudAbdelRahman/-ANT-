# -*- coding: utf-8 -*-
""" 
Python Script
Created on  Sunday August 2017 10:17:41 
@author:  Mahmoud AbdelRahman

[desc]
The sklearn.linear_model module implements generalized linear models. 
It includes Ridge regression, Bayesian Regression, Lasso and Elastic Net estimators 
computed with Least Angle Regression and coordinate descent.
It also implements Stochastic Gradient Descent related algorithms.
[/desc]

ARGUMENTS:  
----------
    <inp> _data : 
        data </inp>
    <inp>_target : 
        target </inp>
    <inp>_features : 
        features </inp>
    <inp>_predict : 
        predict </inp>
    <inp>_algorithm : [optional] - [int] - [12]
        
        Linear Model algorithm 
        Default is 12 i.e. LinearRegression

            Options: 

                1-> ARDRegression ---- Bayesian ARD regression.
                2-> BayesianRidge ---- Bayesian ridge regression
                3-> ElasticNet ---- Linear regression with combined L1 and L2 priors as regularizer.
                4-> ElasticNetCV ---- Elastic Net model with iterative fitting along a regularization path
                5-> Lars ---- Least Angle Regression model a.k.a.
                6-> LarsCV ---- Cross-validated Least Angle Regression model
                7-> Lasso ---- Linear Model trained with L1 prior as regularizer (aka the Lasso)
                8-> LassoCV ---- Lasso linear model with iterative fitting along a regularization path
                9-> LassoLars ---- Lasso model fit with Least Angle Regression a.k.a.
                10-> LassoLarsCV ---- Cross-validated Lasso, using the LARS algorithm
                11-> LassoLarsIC ---- Lasso model fit with Lars using BIC or AIC for model selection
                12-> LinearRegression ---- Ordinary least squares Linear Regression.
                13-> LogisticRegression ---- Logistic Regression (aka logit, MaxEnt) classifier.
                14-> LogisticRegressionCV ---- Logistic Regression CV (aka logit, MaxEnt) classifier.
                15-> MultiTaskLasso ---- Multi-task Lasso model trained with L1/L2 mixed-norm as regularizer
                16-> MultiTaskElasticNet ---- Multi-task ElasticNet model trained with L1/L2 mixed-norm as regularizer
                17-> MultiTaskLassoCV ---- Multi-task L1/L2 Lasso with built-in cross-validation.
                18-> MultiTaskElasticNetCV ---- Multi-task L1/L2 ElasticNet with built-in cross-validation.
                19-> OrthogonalMatchingPursuit ---- Orthogonal Matching Pursuit model (OMP)
                20-> OrthogonalMatchingPursuitCV ---- Cross-validated Orthogonal Matching Pursuit model (OMP)
                21-> PassiveAggressiveClassifier ---- Passive Aggressive Classifier
                22-> PassiveAggressiveRegressor ---- Passive Aggressive Regressor
                23-> Perceptron ---- Read more in the User Guide.
                24-> RandomizedLasso ---- Randomized Lasso.
                25-> RandomizedLogisticRegression ---- Randomized Logistic Regression
                26-> RANSACRegressor ---- RANSAC (RANdom SAmple Consensus) algorithm.
                27-> Ridge ---- Linear least squares with l2 regularization.
                28-> RidgeClassifier ---- Classifier using Ridge regression.
                29-> RidgeClassifierCV ---- Ridge classifier with built-in cross-validation.
                30-> RidgeCV ---- Ridge regression with built-in cross-validation.
                31-> SGDClassifier ---- Linear classifiers (SVM, logistic regression, a.o.) with SGD training.
                32-> SGDRegressor ---- Linear model fitted by minimizing a regularized empirical loss with SGD
                33-> TheilSenRegressor ---- Theil-Sen Estimator: robust multivariate regression model.
                34-> lars_path ---- Compute Least Angle Regression or Lasso path using LARS algorithm [1]
                35-> lasso_path ---- Compute Lasso path with coordinate descent
                36-> lasso_stability_path ---- Stability path based on randomized Lasso estimates
                37-> logistic_regression_path ---- Compute a Logistic Regression model for a list of regularization parameters.
                38-> orthogonal_mp ---- Orthogonal Matching Pursuit (OMP)
                39-> orthogonal_mp_gram ---- Gram Orthogonal Matching Pursuit (OMP)
    </inp>
    <inp>_parameters_ : [optional]
        Parameters of the Linear models - if omitted, it will be set to default values</inp>


RETURN: 
    log_ = output log
    output_ = predict Data
    score_ score value
"""


import numpy as np
import pickle

_data = np.array(_data)
_target = np.array(_target)


def main( _data, _target, _features, _predict, _algorithm = 12):
    ''' This is the main function '''
    allModels = {1:"ARDRegression",                 2:"BayesianRidge",                  3:"ElasticNet",                     4:"ElasticNetCV",
                 5:"Lars",                          6:"LarsCV",                         7:"Lasso",                          8:"LassoCV",
                 9:"LassoLars",                     10:"LassoLarsCV",                   11:"LassoLarsIC",                   12:"LinearRegression",
                 13:"LogisticRegression",           14:"LogisticRegressionCV",          15:"MultiTaskLasso",                16:"MultiTaskElasticNet",
                 17:"MultiTaskLassoCV",             18:"MultiTaskElasticNetCV",         19:"OrthogonalMatchingPursuit",     20:"OrthogonalMatchingPursuitCV",
                 21:"PassiveAggressiveClassifier",  22:"PassiveAggressiveRegressor",    23:"Perceptron",                    24:"RandomizedLasso",
                 25:"RandomizedLogisticRegression", 26:"RANSACRegressor",               27:"Ridge",                         28:"RidgeClassifier",
                 29:"RidgeClassifierCV",            30:"RidgeCV",                       31:"SGDClassifier",                 32:"SGDRegressor",
                 33:"TheilSenRegressor",            34:"lars_path",                     35:"lasso_path",                    36:"lasso_stability_path",
                 37:"logistic_regression_path",     38:"orthogonal_mp",                 39:"orthogonal_mp_gram"}
    try:
        exec("from sklearn.linear_model import "+ allModels[_algorithm]+"\n"
             + "log = "+ allModels[_algorithm]+".__doc__")
        
        exec("model = "+allModels[_algorithm]+"()")
        try:
            model.fit(_data, _target)
            prediction = model.predict(_predict)
            score = model.score(_data, _target)
        except:
            f1 = open(_data, 'r')
            f2 = open(_target, 'r')
            data1 = f1.read()
            target1 = f2.read()
            f1.close()
            f2.close()
            model.fit(pickle.loads(data1), pickle.loads(target1))
            prediction = model.predict(_predict)
            score = model.score(pickle.loads(data1),pickle.loads(target1))
            
    except Exception as e:
        print str(e)
    
    return [log, prediction, score]


if(_data != None and _target!= None and _predict!=None):
    if (_algorithm == None):
        _algorithm = 12

    log_, output_, score_ = main( _data, _target, _features,_predict, _algorithm)
else:
    print "Please Complete all the required data"
