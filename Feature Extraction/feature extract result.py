# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 19:57:02 2021

@author: user
"""
import random
import numpy as np
import tensorflow as tf
import pickle
from tqdm import tqdm, notebook
import os
import time
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input

filenames = pickle.load(open('C:/Users/user/Documents/Data Science Projects/filenames-caltech101.pickle', 'rb'))
feature_list = pickle.load(open('C:/Users/user/Documents/Data Science Projects/features-caltech101-resnet.pickle', 'rb'))

from sklearn.neighbors import NearestNeighbors
neighbors = NearestNeighbors(n_neighbors=5, algorithm='brute', metric='euclidean').fit(feature_list)
distances, indices = neighbors.kneighbors([feature_list[0]])

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

plt.imshow(mpimg.imread(filenames[0]))


plt.imshow(mpimg.imread(filenames[indices[0,1]]))

num_images = 9000 

def plot_image(x):
    for i, y in enumerate(x):
        plt.subplot(1,4,i+1)
        plt.imshow(mpimg.imread(y))
    plt.show()

for i in range(6):
    random_image_index = random.randint(0,num_images)
    distances, indices = neighbors.kneighbors([feature_list[random_image_index]])
# don't take the first closest image as it will be the same image
    similar_image_paths = [filenames[random_image_index]] + [filenames[indices[0][i]] for i in range(1,4)]
    plot_image(similar_image_paths)