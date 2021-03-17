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
M = img.shape[0]
N = img.shape[1]



img1 = img[int(0.14*M):int(0.84*M), int(0.21*N):int(0.73*N)]
cv2.imshow("original image",img1)


ratio = 3
kernel_size = 5
val = 100

low_threshold = val
img_blur = cv2.blur(img1, (3,3))
detected_edges = cv2.Canny(img_blur, low_threshold, low_threshold*ratio, kernel_size)





cv2.imshow("img edg",detected_edges)




cv2.waitKey(0)
cv2.destroyAllWindows()
