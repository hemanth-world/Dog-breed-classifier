# -*- coding: utf-8 -*-
"""Dog Breed Classifier_Test_Data_Evaluation.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1lEFAGuDZkAJ0865cnm6HD1Pn63WlDYur

# Mount the drive
"""

#Connecting this collab notebook to my account.
from google.colab import drive
drive.mount('/content/drive')

"""# Load a saved model
Please change the path value below
"""

import tensorflow as tf
#path of the saved model
loaded_model = tf.keras.models.load_model('/content/drive/MyDrive/AIClub_AP_Addepalli_Hemanth/Project/Best Model/Dog Breed Classifier_spectrogram_model_30_0.001.h5')

"""# Test Images Path"""

# Provide the test path to the folder
src_folder = "/content/drive/MyDrive/AIClub_AP_Addepalli_Hemanth/Project/Dataset/Test"

"""# Dictionary of the labels predicted by the model

"""

import os

#predicted labels
dict_labels = [file for file in os.listdir(src_folder) if os.path.isdir(os.path.join(src_folder, file))]
dict_labels.sort()
dict_labels = dict(enumerate(dict_labels))
print(dict_labels)

"""# Create a list of the images in the test and train folders"""

import os
directory_contents = []
# Find all subfolders in the source folder src_folder
for index in range(0,len(dict_labels)):
  directory_contents.append(dict_labels[index])
print(directory_contents)

# List the files in each subfolder
list_files = []
# Find all the files
for folder_name in directory_contents:
  files_list = os.listdir(os.path.join(src_folder, folder_name))
  list_files.append(files_list)
print(list_files)

"""# Create the predictions and label lists"""

from keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.preprocessing import image
import numpy as np
# A counter to increment after processing each categoty
category_count = 0
# label list
label = []
# Prediction list
predictions = []
y_score = []
for categories in list_files:
  # Create the labels while iterating over each category
  label_temp = np.ones((len(categories))).astype(int)*category_count
  print(label_temp)
  # Add it to existing labels
  label.extend(label_temp)
  for file_name in categories:
    # test image file
    img_path = src_folder + '/' + directory_contents[category_count] + '/' + file_name
    img = image.load_img(img_path, target_size=(224,224))
    img_array = image.img_to_array(img)
    img_batch = np.expand_dims(img_array, axis=0)
    img_preprocessed = preprocess_input(img_batch)
    prediction = loaded_model.predict(img_preprocessed)
    y_score.append(prediction)
    # Save the index of maximum probability
    predictions.append(np.argmax(prediction))
  category_count += 1

"""# Consfusion Matrix"""

from sklearn.metrics import ConfusionMatrixDisplay, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
display_labels = sorted(directory_contents)
plt.figure(figsize = (5,5))
sns.heatmap(confusion_matrix(label,predictions),
            annot = True,
            fmt = 'g',
            cmap = "Blues",
            xticklabels=display_labels,
            yticklabels = display_labels,
            annot_kws={
                'fontsize': 8,
                'fontweight': 'bold',
                'fontfamily': 'serif'
            })
plt.xlabel("Predicted Label")
plt.ylabel("True Label")
plt.title("Confusion Matrix")
#ConfusionMatrixDisplay.from_predictions(label, predictions, display_labels=display_labels, cmap="binary")
plt.show()

"""# Classification Report"""

#classification reports
from sklearn.metrics import classification_report
print(classification_report(label,predictions))