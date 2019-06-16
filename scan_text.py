import cv2
import numpy
import h5py
import keras
from keras.models import load_model
import numpy as np
model = load_model('keras-mnist-model.h5')

def infer(crop):
    image = np.reshape(crop,(-1,28,28,1))
    result = model.predict(image)
    result = result[0]
    #result = list(map(int,result))
    print(result)
    


###CODE

cam = cv2.VideoCapture(0)

while True:
    ret,frame = cam.read()
    key = cv2.waitKey(1)
    flip = cv2.flip(frame,1)
    cv2.rectangle(flip,(50,50),(250,250),(0,0,255),1)
    roi = flip[60:250,60:250]  ## size taken is 190x190
    roi_gray = cv2.cvtColor(roi,cv2.COLOR_BGR2GRAY)
    # thresh = cv2.adaptiveThreshold(roi,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
    _,thresh = cv2.threshold(roi_gray,120,255,cv2.THRESH_BINARY)
    crop = cv2.resize(thresh,(28,28))
    '''
    crop = cv2.imread('./mnist_dream_10.png',0)
    _,thresh2 = cv2.threshold(crop,120,255,cv2.THRESH_BINARY)
    crop = cv2.resize(crop,(28,28))
    cv2.imshow("crop",crop)
    '''
    infer(crop)
    cv2.imshow("frame",roi)
    cv2.imshow("roi",roi_gray)

    if key == ord('x'):
        break

cam.release()
cv2.destroyAllWindows()
