# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 12:55:02 2020

@author: Raj Tagore
"""

import tensorflow as tf
# Importing the Keras libraries and packages
from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense

classifier = Sequential()
classifier.add(Conv2D(32, (3, 3), input_shape=(64, 64, 3), activation = 'relu'))
classifier.add(MaxPooling2D(pool_size=(2, 2)))
