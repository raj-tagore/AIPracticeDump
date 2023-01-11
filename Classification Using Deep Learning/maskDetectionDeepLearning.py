# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 12:27:28 2020

@author: Raj Tagore
"""

import tensorflow as tf
# Importing the Keras libraries and packages
from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
from keras.datasets import fashion_mnist
from keras.utils import to_categorical
import pandas as pd
import numpy as np
from keras.preprocessing import image

mod = Sequential()
mod.add(Conv2D(32, (3, 3), input_shape = (64, 64, 3), activation = 'relu'))
mod.add(MaxPooling2D(pool_size = (2, 2)))
mod.add(Conv2D(32, (3, 3), activation = 'relu'))
mod.add(MaxPooling2D(pool_size = (2, 2)))
mod.add(Flatten())
mod.add(Dense(units = 128, activation = 'relu'))
mod.add(Dense(units = 1, activation = 'sigmoid'))
mod.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

from keras.preprocessing.image import ImageDataGenerator
train_datagen = ImageDataGenerator(rescale = 1./255,
shear_range = 0.2,
zoom_range = 0.2,
horizontal_flip = True)

test_datagen = ImageDataGenerator(rescale = 1./255)

training_set = train_datagen.flow_from_directory(r'D:\Padhai\AI\observations-master\experiements\dest_folder\train',
target_size = (64, 64),
batch_size = 32,
class_mode = 'binary')
  
test_set = test_datagen.flow_from_directory(r'D:\Padhai\AI\observations-master\experiements\dest_folder\test',
target_size = (64, 64),
batch_size = 32,
class_mode = 'binary')

'''trainData = pd.read_csv('train.csv')
testData = pd.read_csv('test.csv')'''

#training_set.class_indices

mod.fit_generator(training_set,
steps_per_epoch = 100,
epochs = 2,
validation_data = test_set,
validation_steps = 80)

print(mod.evaluate(test_set))

