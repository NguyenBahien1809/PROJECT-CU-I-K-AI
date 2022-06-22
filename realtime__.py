pip install opencv-python

import cv2
import numpy as np
import os
from tensorflow.keras.utils import load_img, img_to_array
from keras.models import load_model
predict = {0:'Bacterial Leaf Bright', 1:' Brown Spot',2: 'Healthy', 3:'Leaf Smut'}
model = load_model('disease.h5')
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

org = (30, 170)
# fontScale
fontScale = 1
# Blue color in BGR
color = (0, 0, 255)
font = cv2.FONT_HERSHEY_SIMPLEX
thickness = 2

def predict_img(frame):
    
    img=cv2.resize(frame,(64,64))
    img = img_to_array(img)
    img = img.reshape(1,64,64,3)
    img = img.astype('float32')
    img = img/255
    kq = np.argmax(model.predict(img),axis=-1)
    if(kq==0):
        kq = "Bacterial Leaf Blight "
    if(kq==1):
        kq = "Brown Spot "
    if(kq==2):
        kq = "Healthy"
    if(kq==3):
        kq = "Leaf Smut" 
        
    return kq   
    
	cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    label=predict_img(frame)
    frame=np.ascontiguousarray(np.copy(frame))
    cv2.putText(frame,str(label),org,font,fontScale,color,2)
    cv2.imshow('Frame',frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
            break

cap.release()
# Closes all the frames
cv2.destroyAllWindows()