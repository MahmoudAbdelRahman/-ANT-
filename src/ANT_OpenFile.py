# -*- coding: utf-8 -*-
""" 
Python Script
Created on  Saturday August 2017 05:00:03 
@author:  Mahmoud AbdelRahman

ARGUMENTS:  
    _openFile = Bolean toggle \n To open new File, set _openFile to True.
    output_ = The file full path    
"""
if(_openFile == True):  
    import tkFileDialog
    file_path = tkFileDialog.askopenfilename()
    output_ = file_path
else:  
    output_ = "To open new File, add Toggle True to the input 'OpenFile?'"