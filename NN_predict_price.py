import pandas as pd
import numpy as np
from math import sqrt
from numpy import concatenate
from matplotlib import pyplot
from keras.models import Sequential
from keras.layers import Dense,Activation, BatchNormalization
from keras.layers import Dropout
from keras.callbacks import ModelCheckpoint
from keras.layers import LSTM


from tensorflow.python.client import device_lib
print(device_lib.list_local_devices())
data = pd.read_csv("dataset.csv",delimiter=';')
x=data.drop(['critical','month','day','year','time_h','time_m'],axis=1)[:100000].astype(float)
y=data['critical'].values[:100000]
print(len(y))
data = pd.read_csv("dataset_test.csv",delimiter=';')
x_test=data.drop(['critical','month','day','year','time_h','time_m'],axis=1)[:10000]
y_test=data['critical'].values
print(len(y_test))
# x_train = np.reshape(x, (x.shape[0], x.shape[1]))
# x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1]))
classifier = Sequential()
classifier.add(Dense(units = 20, input_dim=x_train.shape[1]))
# classifier.add(Dropout(0.2))
classifier.add(Dense(units = 20))
classifier.add(Dense(units = 60))
# # classifier.add(Dropout(0.2))
classifier.add(Dense(units = 30))
classifier.add(BatchNormalization())
classifier.add(Dense(units = 1))
classifier.add(Activation('linear'))
classifier.compile(optimizer = 'adam', loss = 'mean_squared_error', metrics = ['accuracy'])

filepath="model/weights-improvement-{epoch:02d}-{acc:.2f}.hdf5"

checkpoint = ModelCheckpoint(filepath, monitor='val_acc', verbose=1, save_best_only=True, mode='max')
callbacks_list = [checkpoint]

history=classifier.fit(x, y,batch_size=32,  epochs = 150,validation_split=0.1, callbacks=callbacks_list)
# score = classifier.evaluate(x_test, y_test)
x_pred = classifier.predict(x_test)
print(x_pred)