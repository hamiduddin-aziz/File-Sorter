import os
import shutil

path = r"D:/Python project/New folder" #your prefered path

print(os.listdir(path)) # to check items in the path
file_names = os.listdir(path)
folder_names = ['csv files', 'image files', 'text files'] # can add your perfered folder here

for folder_name in folder_names:
    folder_path = os.path.join(path, folder_name.strip())
    if not os.path.exists(folder_path):
        print(folder_path)
        os.makedirs(folder_path)

#for the code below you can copy and paste for each type of file in the folder
for file_name in file_names:
    if file_name.endswith('.xlsx'):
        src_path = os.path.join(path, file_name)
        dst_path = os.path.join(path, 'csv files', file_name)
        if not os.path.exists(dst_path):
            shutil.move(src_path, dst_path)

