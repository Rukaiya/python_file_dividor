import os
import shutil
from os import listdir
 
# get the path/directory
folder_dir = "/media/rukaiya/Transcend/OCR/Downloads/20201207/id_card/success"

parent_dir = "/home/rukaiya/Documents"

start = 273
count = 0
output_file = ''

for images in os.listdir(folder_dir):
    if count == 0:
        print(f"start at 0: {start} ")
        os.makedirs(os.path.join(parent_dir, f"Suceess_ID_Card_{start}"))
        shutil.copy(os.path.join(folder_dir, images), os.path.join(parent_dir, f"Suceess_ID_Card_{start}"))

        count += 1

    elif count == 499:
        count = 0
        shutil.copy(os.path.join(folder_dir, images), os.path.join(parent_dir, f"Suceess_ID_Card_{start}"))

        start += 1
        print(f"count: {count}, start: {start}")
    else:
        shutil.copy(os.path.join(folder_dir, images), os.path.join(parent_dir, f"Suceess_ID_Card_{start}"))
        count += 1

    
    

    

