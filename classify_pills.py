import keras
from pypylon import pylon
from keras.models import Model, load_model
from keras.applications.xception import preprocess_input
from keras.utils import multi_gpu_model
from keras.preprocessing import image
import numpy as np
import matplotlib.pyplot as plt
import time
import cv2
import os

def pp_image(img):
    img = image.load_img('pic.png', target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)

    return np.asarray(x)

prediction_list=['capsules',  'oblong',  'other',  'oval',  'round']
model=load_model('models/model.h5', custom_objects={'relu6': mobilenet.relu6})

camera = pylon.InstantCamera(pylon.TlFactory.GetInstance().CreateFirstDevice())

numberOfImagesToGrab = 100
camera.StartGrabbingMax(numberOfImagesToGrab)

converter = pylon.ImageFormatConverter()
converter.OutputPixelFormat = pylon.PixelType_BGR8packed
converter.OutputBitAlignment = pylon.OutputBitAlignment_MsbAligned
i=0
while camera.IsGrabbing():
    time.sleep(0.005)
    grabResult = camera.RetrieveResult(5000, pylon.TimeoutHandling_ThrowException)

    if grabResult.GrabSucceeded():
        # Access the image data.
        print("SizeX: ", grabResult.Width)
        print("SizeY: ", grabResult.Height)
        #import ipdb; ipdb.set_trace()
        img = converter.Convert(grabResult).GetArray()
        cv2.imwrite('pic.png', img)
        pred_img=pp_image(img)
        yo=model.predict(pred_img)
        pred=prediction_list[np.argmax(yo)]
        cv2.putText(img, pred, (100,100), cv2.FONT_HERSHEY_SIMPLEX, 5, (0,0,0), 5, False)
        name='img'+str(i)+'.png'
        cv2.imwrite(os.path.join('prediction_images', name), img)
        i=i+1
        #print("Gray value of first pixel: ", img[0, 0])

    grabResult.Release()
    if i==10:
        break
