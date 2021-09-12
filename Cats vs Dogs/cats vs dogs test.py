# -*- coding: utf-8 -*-
"""
Created on Fri Sep 10 17:25:47 2021

@author: user
"""

import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.layers import Input, Flatten, Dense, Dropout, GlobalAveragePooling2D
from tensorflow.keras.applications.mobilenet import MobileNet, preprocess_input
import math
import numpy as np
from tensorflow.keras.models import load_model
model = load_model('cats_vs_dogs.h5')

#Add path to the image you want to predict
img = tf.keras.preprocessing.image.load_img('C:/Users/user/Downloads/train/dog.6846.jpg', target_size = (224,224))
img_arr = image.img_to_array(img)
ex_img = np.expand_dims(img_arr, axis = 0)
preprocess = preprocess_input(ex_img)

prediction = model.predict(preprocess)
dog = prediction[:, 1]
cat = prediction[:, 0]
if dog > cat:
    print('This image is a dog by probability of', dog*100,'%')
else:
    print('This image is a cat by probability of', cat*100,'%')