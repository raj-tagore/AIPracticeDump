# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 12:15:01 2020

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


mod = Sequential()
mod.add(Conv2D(32, (3, 3), input_shape = (28, 28, 1), activation = 'relu'))
mod.add(MaxPooling2D(pool_size = (2, 2)))
mod.add(Conv2D(32, (3, 3), activation = 'relu'))
mod.add(MaxPooling2D(pool_size = (2, 2)))
mod.add(Flatten())
mod.add(Dense(units = 128, activation = 'relu'))
mod.add(Dense(units = 10, activation = 'softmax'))
mod.compile(optimizer = 'adam', loss = 'categorical_crossentropy', metrics = ['accuracy'])

data = fashion_mnist
#learn and test div
(xl, yl), (xt, yt) = data.load_data()
xl = xl.reshape(60000, 28, 28, 1)
xt = xt.reshape(10000, 28, 28, 1)
yl = to_categorical(yl)
yt = to_categorical(yt)

mod.fit(xl, yl)
loss, acc = mod.evaluate(xt, yt)
print(acc)

