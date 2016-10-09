import os

def rename_files():
    #(1) get file name from a folder
    file_list = os.listdir(r"E:\Udacity\programming-foundations\rename-files-project\prank")
    #print(file_list)
    saved_path = os.getcwd()
    print("Current Working Directory is " + saved_path)
    os.chdir(r"E:\Udacity\programming-foundations\rename-files-project\prank")
    #(2) for each file, rename filename
    for file_name in file_list:
        os.rename(file_name, file_name.strip("0123456789"))
        print("Old Name - " + file_name.strip("0123456789"))
        print("New Name - " + file_name.strip("0123456789"))
    os.chdir(saved_path)
rename_files()