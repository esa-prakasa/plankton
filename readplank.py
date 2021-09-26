# This file is used to read plankton images. The image is then displayed in a new generated window.

import cv2
import os
import numpy as np
import math
import cvzone


os.system("cls")

path = r"C:\Users\Esa\Pictures\_DATASET\plank"

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
#imgIdx = 2

img = cv2.imread(fileList[imgIdx])



M = img.shape[0]
N = img.shape[1]

ratio = M/N

M = 400
N = int(M/ratio)

#img = cv2.resize(img,(int(ratio*N), int(ratio*M)) , interpolation = cv2.INTER_AREA)   
img = cv2.resize(img,(N, M) , interpolation = cv2.INTER_AREA)  

fSz = 3


img = cv2.GaussianBlur(img,(fSz,fSz),0)
cv2.imshow("Original image", img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret,thresh1 = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

#ret,thresh1 = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
cv2.imshow("Original image", thresh1)





cv2.waitKey(0)
cv2.destroyAllWindows()
