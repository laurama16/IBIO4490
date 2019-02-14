#!/usr/bin/python3

import zipfile
import ipdb 
import requests    
import tarfile
import os
import cv2
import scipy.io
from random import *
import numpy as np
from imutils import build_montages
from subprocess import call
import timeit
import pickle
import ipdb
import matplotlib.pyplot as plt
from PIL import ImageFont, ImageDraw, Image
from xlrd import open_workbook
# if it is already downloaded, then do not do it again
if not os.path.isdir(os.path.join(os.getcwd(),'LabPython')):
   url='https://drive.google.com/uc?export=download&id=1BiKTy02isdcUwQPdCMQ2wdBgy_e_ZJDB'
   r=requests.get(url,allow_redirects=True)
   open('Dataset.zip','wb').write(r.content) 
   zip_ref = zipfile.ZipFile('Dataset.zip', 'r')
   zip_ref.extractall()
   zip_ref.close()
#name files inside the directory 
filenames=os.listdir("LabPython/train/")
#random file names selected
rand=sample(filenames,8)
 
#images on the database are too big, so i resized them
#creation of the output directory of the resized images 
if os.path.isdir(os.path.join(os.getcwd(),'Resized')):
    call(['rm', '-r','Resized'])
os.mkdir("Resized")

#obtain the annotations from the excel file
rows = []
level = []
book = open_workbook("LabPython/annot.xlsx")
for sheet in book.sheets():
    for rowidx in range(sheet.nrows):
        row = sheet.row(rowidx)
        for colidx, cell in enumerate(row):
         for i in rand:
            #ipdb.set_trace()
            if str(cell.value)+".jpeg" == i:
                rows.append(rowidx+1)  
                cel = sheet.cell(rowidx, colidx+1) 
                level.append(cel.value)
                
#get the image and groundtruth for the rand file names selected before
imOG=[]
dict={}
dict.setdefault('OG',[])

#go through the random file names and resize the images
cont = 0
for i in rand:
   temp=cv2.imread(os.path.join("LabPython/train/", i))
   #the files are too big. It is necessary to resize
   imCrop=cv2.resize(temp,(300,300))

   # write in the image the corresponding annotation
   cv2_im_rgb = cv2.cvtColor(imCrop, cv2.COLOR_BGR2RGB)
   pil_im = Image.fromarray(cv2_im_rgb)   
   draw = ImageDraw.Draw(pil_im) 
   fontsize = 50
   font = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeMono.ttf", fontsize)
   draw.text((150, 150),str(level[cont]), font=font,fill = (255,255,255))
   
   # Save the image
   cv2_im_processed = cv2.cvtColor(np.array(pil_im), cv2.COLOR_RGB2BGR)
   cv2.imwrite(os.path.join("Resized/",i), cv2_im_processed)
   imCrop= cv2.cvtColor(cv2_im_processed,cv2.COLOR_BGR2RGB)
       
   imOG.append(imCrop)
   dict['OG'].append(imCrop)
   cont = cont+1
   
pickle.dump(dict, open("diccionario.p", "wb"))
montages=build_montages(imOG,(600,400),(4,2))
#Graph
for montage in montages:
    plt.axis("off")
    plt.imshow(montage)
    plt.show()