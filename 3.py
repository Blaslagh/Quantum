# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 20:39:07 2022

@author: Adam
"""
import pandas as pd
import numpy as np

def calc(f_tr="internship_train.csv", f_test="internship_hidden_test"):
    
    data = pd.read_csv(f_tr)
    model = np.polyfit(data['6'], data['target'], 2)
    predict = np.poly1d(model)
    
    x_test = pd.read_csv(f_test+'.csv')
    y_test = predict(x_test['6'])
    pd.DataFrame({'result': y_test}).to_csv(f_test+"_output.csv")
    return