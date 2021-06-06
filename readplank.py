# This file is used to read plankton images. The image is then displayed in a new generated window.

import cv2
import os
import numpy as np
import math

os.system("cls")

path = r"C:\Users\INKOM06\Documents\___KEGIATAN_Ku_2021\_01.19 -- Plankton\images"

fileList = []
with os.scandir(path) as entries:
    for entry in entries:
        fileList.append(entry.name)

N = len(fileList)
for i in range (0,N,1):
	#print(str(i)+"  "+fileList[i])
	fileList[i] = os.path.join(path, fileList[i])
	print(str(i)+" "+fileList[i])


imgIdx = int(input("Give the image index!: "))
img = cv2.imread(fileList[imgIdx])



M = img.shape[0]
N = img.shape[1]
ratio = 0.05

img = cv2.resize(img,(int(ratio*N), int(ratio*M)) , interpolation = cv2.INTER_AREA)   
cv2.imshow("Original image", img)




cv2.waitKey(0)
cv2.destroyAllWindows()
