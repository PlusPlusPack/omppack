from os.path import exists, basename, join, abspath
from os import mkdir, walk
from sys import argv
from zipfile import ZipFile, ZIP_DEFLATED

'''
USE: create_zips.py /path/to/mc/directory

creates zip files for technic solder setup
Extremely primitive right now, must manually
add any extra folders for mods with extra folders
and rename zips by hand'''


def zipDir(zip_dir, zip_file):
    '''Zips all folders and files in a directory with basefolder as base in zip'''
    #adapted from http://coreygoldberg.blogspot.com/2009/07/python-zip-directories-recursively.html
    abs_path = abspath(zip_dir)
    root_len = abs_path.find(basename(abs_path))
    for root, dirs, files in walk(zip_dir):
        archive_root = abspath(root)[root_len:]
        for f in files:
            fullpath = join(root, f)
            archive_name = join(archive_root, f)
            zip_file.write(fullpath, archive_name)

def zipIndvDir(zip_dir, out_dir):
    '''Zips each file in a folder as individual zip, with basefolder as base in zip'''
    #adapted from http://coreygoldberg.blogspot.com/2009/07/python-zip-directories-recursively.html
    abs_path = abspath(zip_dir)
    root_len = abs_path.find(basename(abs_path))
    archive_root = abspath(zip_dir)[root_len:]
    for f in walk(zip_dir).next()[2]:
        zip_file = ZipFile(out_dir + f[:f.rfind(".")] + ".zip", compression=ZIP_DEFLATED, mode='w')
        fullpath = join(zip_dir, f)
        archive_name = join(archive_root, f)
        zip_file.write(fullpath, archive_name)
        zip_file.close()

if __name__ == "__main__":
    basefolder = argv[1]
    if basefolder[-1] != "/":
        basefolder += "/"
    #create output mods directory
    if not exists(basefolder + "solder_mods"):
        mkdir(basefolder + "solder_mods")
    outmods = basefolder + "solder_mods/"
    #zip the configs 
    zipfile = ZipFile(outmods + "z_config.zip", compression=ZIP_DEFLATED, mode='w')
    zipDir(basefolder + "config/", zipfile)
    zipfile.close()
    #traverse mods directory and zip everything
    zipIndvDir(basefolder + "mods/", outmods)
    #traverse the coremods directory and zip everything
    zipIndvDir(basefolder + "coremods/", outmods)
