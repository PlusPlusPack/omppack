from os.path import exists
from os import mkdir, walk, rename
from sys import argv

'''
USE: create_zips.py /path/to/solder/zips/directory

Moves all zips into the file structure required for 
solder to work'''

def folderize(in_dir):
    '''creates folder each file and moves the zip into it'''
    for f in walk(in_dir).next()[2]:
        folder = in_dir + f[:f.find("-")]
        mkdir(folder)
        rename(in_dir + f, folder + "/" + f)

if __name__ == "__main__":
    basefolder = argv[1]
    if basefolder[-1] != "/":
        basefolder += "/"
    folderize(basefolder)
    
