# -*- coding: utf-8 -*-

#Importing necessary libraries

import numpy as np
import pandas as pd
import sklearn.linear_model as skl
from sklearn.model_selection import train_test_split
from sklearn.metrics import explained_variance_score

#Import data into your system from the Link

data = pd.read_csv('https://raw.githubusercontent.com/AdiPersonalWorks/Random/master/student_scores%20-%20student_scores.csv')
data.head() #Outputs first four rows of data

"""
Now the data contains two features, first one is Hours and second one is Scores
We have to predict Scores by using Hours feature.
"""

data.shape #Outputs the shape of data which is (25,2)

model = skl.LinearRegression()

train = data['Hours'] # Separate Train data and Test data
test = data['Scores']

train = train.values.reshape(-1,1)

x_train, x_test, y_train, y_test = train_test_split(train, test, random_state = 42)

#Training the model Now

model.fit(x_train, y_train)

#Testing the model 

y_pred = model.predict(x_test)


#Checking model accuracy

print('The explained variance score is ', explained_variance_score(y_test, y_pred))

#Predicted score for student who studies for 9.25hr/day

sample = np.array(9.25).reshape(1,-1)

print('The predicted score is ', model.predict(sample))
