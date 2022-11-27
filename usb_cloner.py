import shutil
import os

def cloner(src_dir, dest_dir):
    '''
    # path to source directory
    src_dir = 'L:'
    # path to destination directory
    dest_dir = 'C:'
    '''
    # getting all the files in the source directory
    files = os.listdir(src_dir)
    shutil.copytree(src_dir, dest_dir)