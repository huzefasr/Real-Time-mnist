from keras.datasets import mnist
from keras.utils import normalize
from keras.layers import Dense, Activation, Conv2D, Flatten, MaxPooling2D, Dropout
from keras.models import Sequential
import h5py

(train_x,train_y),(test_x,test_y) = mnist.load_data()
train_x = normalize(train_x,1)
test_x = normalize(test_x,1)
model = Sequential()
print(train_x.shape)
#INPUT LAYER
model.add(Conv2D(32,(5,5),input_shape=(28,28,1),activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.25))
#HIDDEN LAYER 1
model.add(Conv2D(64,(5,5),activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
#PREPARING DATA FOR OUTPUT LAYER
model.add(Flatten())
#OUTPUT layer
model.add(Dense(10))
model.add(Activation('softmax'))

model.compile(loss="sparse_categorical_crossentropy",
             optimizer="adam",
             metrics=['accuracy']
             )
train_x = train_x.reshape(train_x.shape[0],28,28,1)
test_x = test_x.reshape(test_x.shape[0],28,28,1)
model.fit(train_x,train_y,epochs=3,validation_data=(test_x,test_y),batch_size=30)
model.save('mnist-test.h5')
