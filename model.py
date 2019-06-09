from keras.datasets import mnist
from keras.utils import normalize
from keras.layers import Dense, Activation, Conv2D, Flatten, MaxPooling2D
from keras.models import Sequential
import h5py

(train_x,train_y),(test_x,test_y) = mnist.load_data()
X = normalize(train_x,1)
model = Sequential()
print(X.shape())
#INPUT LAYER
model.add(Conv2D(32,(5,5),input_shape=X.shape[1:]),activation='relu')
#HIDDEN LAYER 1
model.add(Conv2D(64,(5,5),activation='relu'))
#PREPARING DATA FOR OUTPUT LAYER
model.add(Flatten())
#OUTPUT layer
model.add(Dense(output))
model.add(Activation('sigmoid'))

model.compile(loss="sparse_categorical_crossentropy",
             optimizer="adam",
             metrics=['accuracy']
             )

model.fit(train_x,train_y,test_x,test_y,epochs=1)
model.save('mnist-test.h5')
