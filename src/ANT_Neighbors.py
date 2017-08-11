# -*- coding: utf-8 -*-
""" 
Python Script
Created on  Sunday August 2017 10:17:41 
@author:  Mahmoud AbdelRahman

[desc]
provides functionality for unsupervised and supervised neighbors-based learning methods.
    Unsupervised nearest neighbors is the foundation of many other learning methods, notably manifold learning and spectral clustering.
    Supervised neighbors-based learning comes in two flavors: 
        classification for data with discrete labels, 
        and regression for data with continuous labels.

The principle behind nearest neighbor methods is to find a predefined number of training samples closest in distance to the new point, and predict the label from these.
The number of samples can be a user-defined constant (k-nearest neighbor learning), or vary based on the local density of points (radius-based neighbor learning).
The distance can, in general, be any metric measure: standard Euclidean distance is the most common choice. Neighbors-based methods are known as non-generalizing machine
learning methods, since they simply “remember” all of its training data (possibly transformed into a fast indexing structure such as a Ball Tree or KD Tree.).

Despite its simplicity, nearest neighbors has been successful in a large number of classification and regression problems, including handwritten digits or satellite image scenes.
Being a non-parametric method, it is often successful in classification situations where the decision boundary is very irregular.
The classes in sklearn.neighbors can handle either Numpy arrays or scipy.sparse matrices as input. For dense matrices, a large number of possible distance metrics are supported.
For sparse matrices, arbitrary Minkowski metrics are supported for searches.
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
    <inp>_algorithm : [optional] - [int] - [2]
        
        Decision Tree algorithm 
        Default is 2 i.e. KNeighborsClassifier

            Options: 

                1. (Not Supported Yet) NearestNeighbors -------- Unsupervised learner for implementing neighbor searches. 
                2. KNeighborsClassifier --------  Classifier implementing the k-nearest neighbors vote.
                3. (Not Supported Yet) RadiusNeighborsClassifier --------  Classifier implementing a vote among neighbors within a given radius
                4. KNeighborsRegressor --------   Regression based on k-nearest neighbors.
                5. RadiusNeighborsRegressor --------   Regression based on neighbors within a fixed radius.
                6. NearestCentroid --------   Nearest centroid classifier.
               (IN PROGRESS ... )
                //7. BallTree -------- BallTree for fast generalized N-point problems
                //8. KDTree  -------- KDTree for fast generalized N-point problems
                //9. LSHForest --------   Performs approximate nearest neighbor search using LSH forest.
                //11. KernelDensity--------    Kernel Density Estimation
                //12. kneighbors_graph --------  Computes the (weighted) graph of k-Neighbors for points in X
                //13. radius_neighbors_graph -------- Computes the (weighted) graph of Neighbors for points in X

    </inp>
    <inp>_parameters_ : [optional]
        Parameters of the Neighbors - if omitted, it will be set to default values</inp>


RETURN: 
    log_ = output log
    output_ = predict Data
    score_ score value
"""


import numpy as np
import pickle

_data = np.array(_data)
_target = np.array(_target)


def main( _data, _target, _features, _predict, _algorithm = 2):
    ''' This is the main function '''
    allModels = {   1:"NearestNeighbors",
                    2:"KNeighborsClassifier",
                    3:"RadiusNeighborsClassifier",
                    4:"KNeighborsRegressor",
                    5:"RadiusNeighborsRegressor",
                    6:"NearestCentroid"
                }
    try:
        exec("from sklearn.neighbors import "+ allModels[_algorithm]+"\n"
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
    if (_algorithm == None or _algorithm > 6 or _algorithm <1):
        _algorithm = 2

    if(_algorithm == 1 or _algorithm == 3):
        log_ = "Not supported yet .. stay tuned.."
    else:
        log_, output_, score_ = main( _data, _target, _features,_predict, _algorithm)
else:
    print "Please Complete all the required data"
