# -*- coding: utf-8 -*-
"""
Created on Sat May 15 09:40:26 2021

@author: danish
"""
#This code takes raw profit data and calculates the profit predicted by just providing all expenditures
import numpy as np
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
import sklearn
import sklearn.linear_model
from sklearn.model_selection import train_test_split
from sklearn.metrics import explained_variance_score
data = pd.read_csv("https://raw.githubusercontent.com/amankharwal/Website-data/master/Startups.csv")
train = data.iloc[:,:3].values
test = data['Profit'].values
model = sklearn.linear_model.ElasticNet(l1_ratio=0.6)

x_train,x_test,y_train,y_test = train_test_split(train,test,test_size = 0.2)
model.fit(x_train,y_train)
y_pred = model.predict(x_test)
print('The model variance score is ',explained_variance_score(y_test, y_pred),'\n')
def profit_generator():
    r_d = input('Please Enter R&D expenditures:')
    adm = input("Please Enter administration expenditures:")
    mark = input('Please Enter Marketing expenditures:')
    r_d, adm, mark = int(r_d), int(adm) , int(mark)
    de = np.array([r_d,adm,mark]).reshape(1,-1)
    print('Your Profit Generated is \n')
    return model.predict(de)
print(profit_generator())
    
