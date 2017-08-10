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
import pickle 
import os

directory = "C:/ant/datasets/"

if not os.path.exists(directory):
    os.makedirs(directory)
    
if(_builtInDataset == 1): 
    from sklearn.datasets import load_iris
    data = load_iris()
    data_ = np.array2string(data.data, separator=",")
    target_ = np.array2string(data.target, separator=",")
    features_ = np.array2string(data.target_names, separator=",")

elif(_builtInDataset == 2):  
    from sklearn.datasets import load_boston
    data = load_boston()
    dumpData = pickle.dumps(data.data)
    dumpTargets = pickle.dumps(data.target)
    f = open(directory+"bostonDatadumps.txt", 'w')
    f.write(dumpData)
    f.close()
    
    f2 = open(directory+"bostonTargetdumps.txt", 'w')
    f2.write(dumpTargets)
    f2.close()
    
    data_ = directory+"bostonDatadumps.txt" #np.array2string(data.data, separator=",")
    target_ = directory+"bostonTargetdumps.txt"
    features_ = np.array2string(data.values()[1], separator=",")

elif(_builtInDataset == 3):  
    from sklearn.datasets import load_diabetes
    data = load_diabetes()
    print data.data.shape
    dumpData = pickle.dumps(data.data)
    dumpTargets = pickle.dumps(data.target)
    f = open(directory+"diabetesDatadumps.txt", 'w')
    f.write(dumpData)
    f.close()
    
    f2 = open(directory+"diabetesTargetdumps.txt", 'w')
    f2.write(dumpTargets)
    f2.close()
    
    data_ = directory+"diabetesDatadumps.txt"
    target_ = directory+"diabetesTargetdumps.txt"
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