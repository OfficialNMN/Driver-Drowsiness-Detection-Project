import os
from tensorflow import keras
from tensorflow.keras.preprocessing import image
import matplotlib.pyplot as plt 
import numpy as np
from tensorflow.keras.utils.np_utils import to_categorical
import random,shutil
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dropout,Conv2D,Flatten,Dense, MaxPooling2D, BatchNormalization
from tensorflow.keras.models import load_model


def generator(dir, gen=image.ImageDataGenerator(rescale=1./255), shuffle=True,batch_size=1,target_size=(24,24),
              class_mode='categorical' ):

    return gen.flow_from_directory(dir,batch_size=batch_size,shuffle=shuffle,color_mode='grayscale',
                                   class_mode=class_mode,target_size=target_size)

batch= 32
target=(24,24)
train_batch = generator(data_dir,shuffle=True, batch_size=batch,target_size=target)
valid_batch = generator(data_dir,shuffle=True, batch_size=batch,target_size=target)
size_per_epoch= len(train_batch.classes)//batch
validation_size = len(valid_batch.classes)//batch
print(size_per_epoch,validation_size)
Using Basic CNN Architecture
model = Sequential([
    Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(24,24,1)),
    MaxPooling2D(pool_size=(1,1)),
    Conv2D(32,(3,3),activation='relu'),
    MaxPooling2D(pool_size=(1,1)),
    #32 convolution filters used each of size 3x3 again
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D(pool_size=(1,1)),
    #64 convolution filters used each of size 3x3 choose the best features via pooling
    #randomly turn neurons on and off to improve convergence
    Dropout(0.25),
    #flatten since too many dimensions, we only want a classification output
    Flatten(),
    #fully connected to get all relevant data
    Dense(128, activation='relu'),
    #one more dropout for convergence' sake :) 
    Dropout(0.5),
    #output a softmax to squash the matrix into output probabilities
    Dense(2, activation='softmax')
])
model.summary()
model.compile(optimizer='adam',loss='categorical_crossentropy',metrics=['accuracy'])

model.fit_generator(train_batch, validation_data=valid_batch,epochs=2,steps_per_epoch=Size_per_epoch ,validation_steps=validation_size)
model.save('CNN_Drowsiness.h5')
