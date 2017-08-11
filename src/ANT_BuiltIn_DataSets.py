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




def main(dataSet):
    ''' This is the main function  '''

    directory = "C:/ant/datasets/"
    if not os.path.exists(directory):
        os.makedirs(directory)


    allDataSets = { 1:"load_iris",     2:"load_boston",    3:"load_digits",
                    4:"load_diabetes"}
    try:
        exec("from sklearn.datasets import "+allDataSets[dataSet])
        exec("data = "+allDataSets[dataSet]+"()")

        dumpData = pickle.dumps(data.data)
        dumpTargets = pickle.dumps(data.target)
        f = open(directory+allDataSets[dataSet]+"_Data.txt", 'w')
        f.write(dumpData)
        f.close()
        
        f2 = open(directory+allDataSets[dataSet]+"_Target.txt", 'w')
        f2.write(dumpTargets)
        f2.close()
        
        data = directory+allDataSets[dataSet]+"_Data.txt" #np.array2string(data.data, separator=",")
        target = directory+allDataSets[dataSet]+"_Target.txt"
        featuers = None
        return [data, target, featuers]
    except Exception as e:
        print str(e)


if(_builtInDataset != None):
    data_, target_, features_ = main(_builtInDataset)
