# -*- coding: utf-8 -*-
""" 
Python Script
Created on  Sunday August 2017 10:17:41 
@author:  Mahmoud AbdelRahman

[desc]
Support vector machines (SVMs) are a set of supervised learning methods used for classification, regression and outliers detection.

The advantages of support vector machines are:

    - Effective in high dimensional spaces. 
    - Still effective in cases where number of dimensions is greater than the number of samples. 
    - Uses a subset of training points in the decision function (called support vectors), so it is also memory efficient. 
    - Versatile: different Kernel functions can be specified for the decision function. Common kernels are provided, but it is also possible to specify custom kernels. 

The disadvantages of support vector machines include:

    - If the number of features is much greater than the number of samples, the method is likely to give poor performances. 
    - SVMs do not directly provide probability estimates, these are calculated using an expensive five-fold cross-validation. 
    
The support vector machines in scikit-learn support both dense (numpy.ndarray and convertible to that by numpy.asarray) and sparse (any scipy.sparse) sample vectors as input. However, to use an SVM to make predictions for sparse data, it must have been fit on such data. For optimal performance, use C-ordered numpy.ndarray (dense) or scipy.sparse.csr_matrix (sparse) with dtype=float64.
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
                1->Support Vector Classifier SVC
                2->Linear Support Vector Classifier LinSVC
                3->Nu Support Vector Classifier NuSVC
                4->Support Vector Regression SVR
                5->Linear Support Vector Regression LinSVR
                6->Nu Support Vector Regression NuSVR
                7->One Class Support Vector Machines
    </inp>
    <inp>_parameters_ : [optional]
        Parameters of the Support Vector Machine Model, such as :
        C, kernel, degree, gamma, coef0, probability, shrinking, tol, chach_size, class_weight, verbose, max_iter
        ,decision_function_shape and random_state</inp>


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
    
    allModels ={1:"SVC",        2:"LinearSVC",          3:"NuSVC",
                4:"SVR",        5:"LinearSVR",          6:"NuSVR",
                7:"OneClassSVM"}

    if(_algorithm == None):
        _algorithm =1 
    
    try:
        exec("from sklearn.svm import "+ allModels[_algorithm]+"\n"
             + "log = "+ allModels[_algorithm]+".__doc__")
        
        exec("model = "+allModels[_algorithm]+"()")
        try:
            model.fit(_data, _target)
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