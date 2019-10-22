from zipfile import ZipFile 
import sys  
import numpy as np
import pandas as pd
import os
import tempfile
from zipfile import ZipFile 
import shutil

# specifying the zip file name 
file_name = sys.argv[1]

#making Temp Folder
tempfile.mkdtemp('temp',)

i = 0

# extracting all the files to temp folder
with ZipFile(file_name, 'r') as First:
    First.extractall(path='temp')
    path = os.getcwd()
    Dpath = path +'/'+file_name[:-4]
    os.mkdir(Dpath)
    #identifying all unique names of files in each individual zip file
    for name in First.namelist():
        data = First.read(name)
        #extracting individual files to newly create folder
        with ZipFile('temp/'+ name, 'r') as zip: 
            zip.extractall(path=Dpath)
            if i < 1:
              TxtFilenames = os.listdir(Dpath)
              i = i + 1
              #renames files accordingly based on outer layers of zip files
            for filename in TxtFilenames: 
              src =Dpath +'/'+ filename
              dst =Dpath +'/'+ filename[:-4]+'_'+file_name[10:14] +name[6:10]+'.txt'
              try:
                os.rename(src, dst) 
              except:
                #reports if a individual file is missing
                print('Source File Not Found: '+ dst)
                continue


shutil.rmtree('temp')
print('All Files are located in: '+ Dpath)
print('Done!') 