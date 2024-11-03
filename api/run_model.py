import urllib
import urllib.request
import numpy as np
import cv2
from tensorflow.keras.models import load_model

model = load_model('model/wildfire_classifier_model.h5')


# takes url and outputs the img data to be used in the predict img fn
def fetch_img(url):
    req = urllib.request.urlopen(url)
    data = np.asarray(bytearray(req.read()), dtype=np.uint8)

    img = cv2.imdecode(data, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (128, 128))
    img = img.astype('float32') / 255.0
    img = np.reshape(img, (1, 128, 128, 1)) 

    return img

def predict_img(url):
    global model
    img = fetch_img(url)
    prediction = model.predict(img)
    label = "Wildfire" if prediction[0] > 0.5 else "Not Wildfire"
    return label
