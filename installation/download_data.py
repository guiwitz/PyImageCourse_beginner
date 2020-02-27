import sys, os, zipfile, tarfile
import urllib.request
import requests

where_to_save = 'Data/'

#create data directory
if not os.path.exists(where_to_save):
    os.makedirs(where_to_save)

url = 'http://wiki.cmci.info/sampleimages/cells_Actin.tif'  
urllib.request.urlretrieve(url, where_to_save+'cells_Actin.tif')

url = 'https://cildata.crbs.ucsd.edu/media/images/13901/13901.tif' 
urllib.request.urlretrieve(url, where_to_save+'yeast.tif')

url = 'https://cildata.crbs.ucsd.edu/media/images/48102/48102.tif' 
urllib.request.urlretrieve(url, where_to_save+'3colors.tif')

url = 'https://cildata.crbs.ucsd.edu/media/images/13585/13585.tif' 
urllib.request.urlretrieve(url, where_to_save+'myoblast.tif')

url = 'https://cildata.crbs.ucsd.edu/media/images/13586/13586.tif' 
urllib.request.urlretrieve(url, where_to_save+'myoblast2.tif')

url = 'https://cildata.crbs.ucsd.edu/media/images/13590/13590.tif' 
urllib.request.urlretrieve(url, where_to_save+'myoblast3.tif')