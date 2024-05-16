import os
import shutil

basepath=r"C:\\codewithharry\\python\\e7-clear the clutter"
files=os.listdir("C:\\codewithharry\\python\\e7-clear the clutter")

for file in files:
    print(file)
    ext=file.split(".")[-1]
    print(ext)
    if(ext!="py" and len(file.split("."))>1):
        new_dir_path=os.path.join(basepath,ext)#this makes a new directory named after the file extension
        current_path=os.path.join(basepath,file)#this creates a current path of the file so that it will be easy to make it move from here.
        new_path=os.path.join(new_dir_path,file)#creates a new path so that if the directory exist by the ext name then it will be moved from its current path to the new path.

        if os.path.exists(new_dir_path):
            shutil.move(current_path,new_path)

        else:
            os.makedirs(new_dir_path)
            shutil.move(current_path,new_path)

