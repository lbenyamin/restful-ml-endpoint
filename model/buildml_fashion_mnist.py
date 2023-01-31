# -*- coding: utf-8 -*-
"""buildml-fashion-mnist.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1S5PMxVUymiu_6Wy_GX6vngfjEkxsEIem

# Build ML Fashion MNIST
"""


import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

x_train1 = pd.read_csv('C:/Users/lucas/Documents/GitHub/restful-ml-endpoint/data/fashion-mnist-train-1.csv')
print(x_train1)

x_train2 = pd.read_csv('C:/Users/lucas/Documents/GitHub/restful-ml-endpoint/data/fashion-mnist-train-2.csv')
print(x_train2)

x_test = pd.read_csv('C:/Users/lucas/Documents/GitHub/restful-ml-endpoint/data/fashion-mnist_test.csv')
print(x_test)

"""## Preprocessing"""

labels = {0 : "T-shirt/top", 1: "Trouser", 2: "Pullover", 3: "Dress", 4: "Coat",
          5: "Sandal", 6: "Shirt", 7: "Sneaker", 8: "Bag", 9: "Ankle Boot"}
print(labels)

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

print("Fashion MNIST train 1 -  rows:",x_train1.shape[0]," columns:", x_train1.shape[1])
print("Fashion MNIST train 2 -  rows:",x_train2.shape[0]," columns:", x_train2.shape[1])
print("Fashion MNIST test -  rows:",x_test.shape[0]," columns:", x_test.shape[1])

from tensorflow.python import keras
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense, Flatten, Conv2D, Dropout, MaxPooling2D

x_image1 = x_train1.drop(columns='label').to_numpy()
y_test = x_test.drop(columns='label').to_numpy()
x_image2 = x_train2.drop(columns='label').to_numpy()

x_image1

print(len(x_image1))
print(len(y_test))
print(len(x_image2))

x_label1 = x_train1["label"]
y_label = x_test["label"]
x_label2 = x_train2["label"]

x_label1

y_label.shape

len(y_label)

x_image1 = x_image1 / 255.0

y_test = y_test / 255.0

x_image2 = x_image2 / 255.0

model = tf.keras.Sequential([
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(10)
])

model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

"""# For MNIST train 2"""

model2 = model.fit(x_image2, x_label2, epochs=50)

model.summary()

test_loss, test_acc = model.evaluate(y_test,  y_label, verbose=2)

print('\nTest accuracy:', test_acc)

probability_model = tf.keras.Sequential([model, 
                                         tf.keras.layers.Softmax()])

predictions = probability_model.predict(y_test)

predictions[0]

np.argmax(predictions[0])

y_label[0]

model.save('model_train2.h5')
print(type(x_image2))
df1 = arr.item(0)
print(df1)
df1.to_json("C:/Users/lucas/Documents/GitHub/restful-ml-endpoint/data/test.json")

"""# For MNIST train 1"""

model1 = model.fit(x_image1, x_label1, epochs=50)

