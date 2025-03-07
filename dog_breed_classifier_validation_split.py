# -*- coding: utf-8 -*-
"""dog breed classifier validation_split.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/18aiIfyQaOEYIkpSkjbsgjRm25EffRSt4

## Mount Google Drive locally
"""

from google.colab import drive
drive.mount('/content/drive')

"""## Path to source and destination folder

- You should have created a validation image folder before moving further.
"""

import os

# Provide the source folder
src_folder = "/content/drive/MyDrive/AIClub_AP_Addepalli_Hemanth/Project/Dataset/Train"
# Provide the destination folder
dest_folder = "/content/drive/MyDrive/AIClub_AP_Addepalli_Hemanth/Project/Dataset/Test"

"""## List sub-folders"""

# Find all subfolders in the source folder src_folder
directory_contents = os.listdir(src_folder)
print('directory_contents: ', directory_contents)

# Append the path of the src_folder with the sub-folders
sub_folders = []
for item in directory_contents:
  if os.path.isdir(os.path.join(src_folder,item)):
    sub_folders.append(item)
print('sub_folders: ', sub_folders)

"""# Create duplicate folder structure"""

# Create the same folder structure in destination
for folder_name in sub_folders:
  os.mkdir(os.path.join(dest_folder,folder_name))

"""## List the files"""

# List full paths of all images in each category/sub-folder
list_files = []
# Find all the files, note that you have to change it to tif if that is the extension
for folder_name in directory_contents:
  files_list = [_ for _ in os.listdir(os.path.join(src_folder, folder_name))]
  # Create the list with full path
  full_path_files_list = []
  for file_name in files_list:
    full_path_files_list.append(os.path.join(src_folder, folder_name, file_name))
  list_files.append(full_path_files_list)
print(list_files[1])

"""## Move x% of files"""

import random

# Specify the fraction
#this is the splitting percentage. 10% will be sent to validation
x = 10

for files_list in list_files:
  # length of the list
  list_len = len(files_list)
  # length of x%
  frac_len = int(list_len * (x/100))
  # select x% of files
  files_to_move = random.sample(files_list, frac_len)
  for single_file in files_to_move:
    # extract the sub-string with subfolder/category and file name
    subfolder_file = '/'.join(single_file.split('/')[-2:])
    # destination path
    dst_folder = os.path.join(dest_folder, subfolder_file)
    # Move the file
    os.replace(single_file, dst_folder)

for folder_name in sub_folders:
  print(folder_name, len(os.listdir(os.path.join(dest_folder,folder_name))))