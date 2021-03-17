import cv2
import os
import numpy as np
import math

os.system("cls")

fullPath = r"C:\Users\INKOM06\Pictures\_DATASET\Pari19\Developed-Bacteriastrum furcatum (400X) PariIslandRisetPro19 St10.jpg"

img = cv2.imread(fullPath)
ratio = 0.2
M = img.shape[0]
N = img.shape[1]

img = cv2.resize(img, (int(ratio*N),int(ratio*M)),interpolation = cv2.INTER_AREA)

img1 = img[100:580, 220:760]

ret,th1 = cv2.threshold(img1,200,255,cv2.THRESH_BINARY)

cv2.imshow("img",th1)




cv2.waitKey(0)
cv2.destroyAllWindows()
