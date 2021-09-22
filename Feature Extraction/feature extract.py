# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 18:33:33 2021

@author: user
"""

import numpy as np
import tensorflow as tf
import pickle
from tqdm import tqdm, notebook
import os
import time
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input

model = ResNet50(include_top=False, input_shape=(224,224,3))
def extract_features(img_path, model):
    input_shape = (224, 224, 3)
    img = image.load_img(img_path, target_size=(input_shape[0], input_shape[1]))
    img_array = image.img_to_array(img)
    expanded_img_array = np.expand_dims(img_array, axis=0)
    preprocessed_img = preprocess_input(expanded_img_array)
    features = model.predict(preprocessed_img)
    flattened_features = features.flatten()
    normalized_features = flattened_features / np.linalg.norm(flattened_features)
    return normalized_features


extensions = ['.jpg', '.png', '.jpeg', '.PNG', '.JPEG', '.JPG']
def get_flist(rootdir):
    flist = []
    counter = 1
    for root, directory, filename in os.walk(rootdir):
        for fname in filename:
            flist.append(os.path.join(root,fname))
            counter +=1
    print(counter)            
    return flist
rootdir = 'C:/Users/user/Downloads/Categories'
file_name = sorted(get_flist(rootdir))

feature_list = []
for i in tqdm(range(len(file_name))):
    feature_list.append(extract_features(file_name[i], model))
    
pickle.dump(feature_list, open('features-caltech101-resnet.pickle', 'wb'))
pickle.dump(file_name, open('filenames-caltech101.pickle','wb'))