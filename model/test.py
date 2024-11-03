# import the model;

# import the image processing function


# build function - fetch_image
# input: image url
# output: image data
import urllib
import urllib.request
import numpy as np

req = urllib.request.urlopen("https://earthengine.googleapis.com/v1/projects/ee-neelrages/thumbnails/b3684cd21ef7ca3f11318f89c353a96a-5e39e5d50330fe7dcc0ee1e420c41313:getPixels")
data = np.asarray(bytearray(req.read()), dtype=np.uint8)

# pass this into image processing .

import cv2
img = cv2.imdecode(data, -1)
img = cv2.resize(img, (128, 128))
img = img.astype('float32') / 255

print(img.flatten().shape)
# print(data)

# import predict function

# build new function: predict_image
# input: image url
# output: class

# change image url to image data
# take image darta and process
# take flattened image and run predict_image imported function

# return the result

