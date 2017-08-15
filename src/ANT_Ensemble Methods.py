# -*- coding: utf-8 -*-
""" 
ANT_
Created on  Tuesday August 15 2017 11:01:22 
@author:  Mahmoud AbdelRahman

[name]ANT_Ensemble Methods[/name]

[desc]
    The goal of ensemble methods is to combine the predictions of 
several base estimators built with a given learning algorithm in 
order to improve generalizability robustness over a single estimator.
    
        Two families of ensemble methods are usually distinguished:

            1. In averaging methods, the driving principle is to build several
        estimators independently and then to average their predictions. On
        average, the combined estimator is usually better than any of the
        single base estimator because its variance is reduced.
        Examples: Bagging methods, Forests of randomized trees,

            2. By contrast, in boosting methods, base estimators are built
        sequentially and one tries to reduce the bias of the combined
        estimator. The motivation is to combine several weak models to
        produce a powerful ensemble.
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
    <inp>_algorithm : [optional] - [int] - [1]
        Support Vector Machines Algorithm
            Options: 
                1.AdaBoostClassifier ---------------- An AdaBoost classifier.
                2.AdaBoostRegressor  ---------------- An AdaBoost regressor.
                3.BaggingClassifier  ---------------- A Bagging classifier.
                4.BaggingRegressor------------------- A Bagging regressor.
                5.ExtraTreesClassifier -------------- An extra-trees classifier.
                6.ExtraTreesRegressor --------------- An extra-trees regressor.
                7.GradientBoostingClassifier -------- Gradient Boosting for classification.
                8.GradientBoostingRegressor --------- Gradient Boosting for regression.
                9.IsolationForest  ------------------ Isolation Forest Algorithm
                10.RandomForestClassifier ----------- A random forest classifier.
                11.RandomForestRegressor ------------ A random forest regressor.
                12.RandomTreesEmbedding ------------- An ensemble of totally random trees.
                13.VotingClassifier ----------------- Soft Voting/Majority Rule classifier for unfitted estimators.
    </inp>
    <inp>_parameters_ : [optional]
        Parameters of the Ensemble Methods :
        </inp>


RETURN: 
    log_ = output log
    output_ = predict Data
    score_ score value
"""


import numpy as np
import pickle

_data = np.array(_data)
_target = np.array(_target)


def main( _data, _target, _features, _algorithm = 1):
    ''' this is the main function ''' 
    
    allModels ={1:"AdaBoostClassifier",
                2:"AdaBoostRegressor",
                3:"BaggingClassifier",
                4:"BaggingRegressor",
                5:"ExtraTreesClassifier",
                6:"ExtraTreesRegressor",
                7:"GradientBoostingClassifier", 
                8:"GradientBoostingRegressor",
                9:"IsolationForest",
                10:"RandomForestClassifier",
                11:"RandomForestRegressor",
                12:"RandomTreesEmbedding",
                13:"VotingClassifier"}

    if(_algorithm == None):
        _algorithm =1 
    
    try:
        exec("from sklearn.ensemble import "+ allModels[_algorithm]+"\n"
             + "log = "+ allModels[_algorithm]+".__doc__")
        
        exec("model = "+allModels[_algorithm]+"()")
        try:
            model.fit(_data, _target)
            if _features != None:
                prediction = _features[model.predict(_predict)]
            else:
                prediction = model.predict(_predict)
            try:
                score = model.score(_data, _target)
            except:
                score = "Not defined"
        except:
            f1 = open(_data, 'r')
            f2 = open(_target, 'r')
            data1 = f1.read()
            target1 = f2.read()
            f1.close()
            f2.close()
            model.fit(pickle.loads(data1), pickle.loads(target1))
            if _features != None:
                try:
                    prediction = _features[model.predict(_predict)]
                except:
                    prediction = model.predict(_predict)
            else:
                prediction = model.predict(_predict)
            try:
                score = model.score(pickle.loads(data1),pickle.loads(target1))
            except:
                score = "Not defined"
            
    except Exception as e:
        print str(e)
    
    return [log, prediction, score]

if(_data != None and _target!= None and _predict!=None):
    log_, output_, score_ = main( _data, _target, _features, _algorithm)
else:
    print "Please Complete all the required data"
