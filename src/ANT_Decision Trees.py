# -*- coding: utf-8 -*-
""" 
Python Script
Created on  Sunday August 2017 10:17:41 
@author:  Mahmoud AbdelRahman

[desc]
Decision Trees (DTs) are a non-parametric supervised learning method used for classification and regression.

The goal is to create a model that predicts the value of a target variable by learning simple decision rules inferred from the data features.
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
        
        Decision Tree algorithm 
        Default is 1 i.e. DecisionTreeClassifier

            Options: 

                1. DecisionTreeClassifier ------ A decision tree classifier.
                2. DecisionTreeRegressor  ------  A decision tree regressor.
                3. ExtraTreeClassifier ------   An extremely randomized tree classifier.
                4. ExtraTreeRegressor ------    An extremely randomized tree regressor.

    </inp>
    <inp>_parameters_ : [optional]
        Parameters of the DecisionTree - if omitted, it will be set to default values</inp>


RETURN: 
    log_ = output log
    output_ = predict Data
    score_ score value
"""


import numpy as np
import pickle

_data = np.array(_data)
_target = np.array(_target)


def main( _data, _target, _features, _predict, _algorithm = 1):
    ''' This is the main function '''
    allModels = {   1:"DecisionTreeClassifier",
                    2:"DecisionTreeRegressor",
                    3:"ExtraTreeClassifier",
                    4:"ExtraTreeRegressor"
                }
    try:
        exec("from sklearn.tree import "+ allModels[_algorithm]+"\n"
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
    if (_algorithm == None or _algorithm > 4):
        _algorithm = 1


    log_, output_, score_ = main( _data, _target, _features,_predict, _algorithm)
else:
    print "Please Complete all the required data"
