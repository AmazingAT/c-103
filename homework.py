import os
import shutil

from_dir="C:/Users/dell/Downloads"
to_dir="C:/Users/dell/Downloads/C-102"

listof_files=os.listdir(from_dir)
# print(listof_files)
for file_name in listof_files:
    name,extension = os.path.splitext(file_name)
    # print(name)
    # print(extension)
    if extension=="":
        continue
    if extension in [".pdf",".pptx",".docx"]:
        path_1=from_dir+"/"+file_name
        path_2=to_dir+"/"+"files"
        path_3=to_dir+"/"+"files"+"/"+file_name
        if os.path.exists(path_2):
            print("Moving"+file_name)
            shutil.move(path_1,path_3)
        else:
            os.makedirs(path_2)
            print("Moving"+file_name)
            shutil.move(path_1,path_3)