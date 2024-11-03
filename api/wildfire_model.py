import cv2
import numpy as np
import os
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.optimizers import Adam

train_input_folder_wildfire = '/Users/chasecoogan/Documents/bu/model/datasets/wildfire/train/wildfire'
train_input_folder_no_wildfire = '/Users/chasecoogan/Documents/bu/model/datasets/wildfire/train/nowildfire'
test_input_folder_wildfire = '/Users/chasecoogan/Documents/bu/model/datasets/wildfire/test/wildfire'
test_input_folder_no_wildfire = '/Users/chasecoogan/Documents/bu/model/datasets/wildfire/test/nowildfire'

image_size = (128, 128)

def convert_img_to_greyscale(directory, label):
    images = []
    labels = []
    for ea in os.listdir(directory):
        if ea.endswith(".jpg"):
            path = os.path.join(directory, ea)
            img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
            img = cv2.resize(img, image_size)
            img = img.astype('float32') / 255
            images.append(img)
            labels.append(label)
    return images, labels

def prepare_data():
    train_images_wildfire, train_labels_wildfire = convert_img_to_greyscale(train_input_folder_wildfire, label=1)
    train_images_no_wildfire, train_labels_no_wildfire = convert_img_to_greyscale(train_input_folder_no_wildfire, label=0)
    test_images_wildfire, test_labels_wildfire = convert_img_to_greyscale(test_input_folder_wildfire, label=1)
    test_images_no_wildfire, test_labels_no_wildfire = convert_img_to_greyscale(test_input_folder_no_wildfire, label=0)

    train_images = np.array(train_images_wildfire + train_images_no_wildfire).reshape(-1, 128, 128, 1)
    train_labels = np.array(train_labels_wildfire + train_labels_no_wildfire)
    test_images = np.array(test_images_wildfire + test_images_no_wildfire).reshape(-1, 128, 128, 1)
    test_labels = np.array(test_labels_wildfire + test_labels_no_wildfire)
    
    return train_images, train_labels, test_images, test_labels

def build_model():
    model = Sequential([
        Conv2D(32, (3, 3), activation='relu', input_shape=(128, 128, 1)),
        MaxPooling2D((2, 2)),
        Conv2D(64, (3, 3), activation='relu'),
        MaxPooling2D((2, 2)),
        Conv2D(128, (3, 3), activation='relu'),
        MaxPooling2D((2, 2)),
        Flatten(),
        Dense(128, activation='relu'),
        Dropout(0.5),
        Dense(1, activation='sigmoid')
    ])
    model.compile(optimizer=Adam(), loss='binary_crossentropy', metrics=['accuracy'])
    return model

def train_and_evaluate():
    train_images, train_labels, test_images, test_labels = prepare_data()
    model = build_model()
    model.fit(train_images, train_labels, epochs=10, batch_size=32, validation_data=(test_images, test_labels))
    test_loss, test_accuracy = model.evaluate(test_images, test_labels)
    print("Test accuracy:", test_accuracy)
    return model

def predict_img_class(model, img_path):
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (128, 128))
    img = img.astype('float32') / 255.0
    img = np.reshape(img, (1, 128, 128, 1))
    prediction = model.predict(img)
    return "Wildfire" if prediction[0] > 0.5 else "Not Wildfire"
