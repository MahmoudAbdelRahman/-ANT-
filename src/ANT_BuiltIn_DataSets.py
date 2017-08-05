# -*- coding: utf-8 -*-
""" 
Python Script
Created on  Thursday August 2017 11:25:50 
@author:  Mahmoud AbdelRahman 

    ARGUMENTS:  
        _builtInDataset = Set of built-in datasets \n1 ->Iris_dataset\n2 ->Boston_dataset\n3 ->Diabetes dataset[not available yet]\n4 ->Digits dataset

    RETURN:  
        data_     = The data of the instances
        target_   = Targets of the data
        features_ = Target names

"""
import numpy as np

if(_builtInDataset == 1): 
    from sklearn.datasets import load_iris
    data = load_iris()
    data_ = np.array2string(data.data, separator=",")
    target_ = np.array2string(data.target, separator=",")
    features_ = np.array2string(data.target_names, separator=",")

elif(_builtInDataset == 2):  
    from sklearn.datasets import load_boston
    data = load_boston()
    data_ = np.array2string(data.data, separator=",")
    target_ = np.array2string(data.target, separator=",")
    features_ = np.array2string(data.values()[1], separator=",")

elif(_builtInDataset == 3):  
    from sklearn.datasets import load_diabetes
    data = load_diabetes()
    alldata = []
    for i in data.data:  
        alldata.append(i)
    data_ = str(alldata).replace("array(", "").replace("])", "]")
    target_ = np.array2string(data.target, separator=",")
    features_ = None

elif(_builtInDataset == 4): 
    #this block requires more work for efficiency purposes, may be dumps and loads	
    """from sklearn.datasets import load_digits
    data = load_digits()
    alldata = []
    alltargets = []
    for i in data.data:  
        alldata.append(i)
    for i in data.target:  
        alltargets.append(i)"""
    data_ = None
    target_ = None
    features_ = None