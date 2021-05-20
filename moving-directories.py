#This script was made to create copies of files/diretories from a directory to another.

import os
import shutil

source = 'C:\\Users\\conta\\Desktop\\programming_stuff\\Lucia' #Path to where the script will search the names given.
dest = 'C:\\Users\\conta\\Desktop\\programming_stuff\\Lucia\\selected' #Where the copies will be saved.

def get(*args):
    """Copy directories/files"""
    files_already_in_folder = []
    global source
    global dest
    for i in args:
        name = i #based on "name", move directory/file from source to dest

        for file in os.listdir(source + "/" + name):
            try:
                text = os.path.join(source, name, file)
                filtered = os.path.join(dest, file)
                shutil.copytree(text, filtered)
            except FileExistsError: #In case it finds a directory/file with the same name, the copy receives the source ending.
                shutil.copytree(text, filtered + "_" + name)
                print("Name {} already in use.".format(file) + " New copy saved as {}.".format(file + "_" + name))
                files_already_in_folder.append(file)
    return files_already_in_folder

files_already_in_folder = get("1995", "1996", "1997", "1998", "1999")
