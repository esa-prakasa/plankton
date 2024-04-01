# Warna segmentasi tidak benar-benar berbeda
# Lebih baik dibuat 3 kelas saja, plankton, overlap, dan bukan plankton
# ukuran antara image RGB dan mask berbeda
# Sebaiknya dibuat slide yang tunjukkan pasangan image RGB dan mask yang dibuat



import cv2 
import os
import numpy as np

os.system("cls")

pathRGB = r'C:\Users\HP\Pictures\plankton\rgb'
pathMask = r'C:\Users\HP\Pictures\plankton\mask'

rgbFiles = os.listdir(pathRGB)
maskFiles = os.listdir(pathMask)


idx = 0
rgb = cv2.imread(os.path.join(pathRGB,rgbFiles[idx]))
mask = cv2.imread(os.path.join(pathMask,maskFiles[idx]))


M = mask.shape[0]
N = mask.shape[1]

ratio = 0.3
new_M = round(ratio*M)
new_N = round(ratio*N)

rgb = cv2.resize(rgb, (new_N, new_M))
segP1 = rgb.copy()
segP2 = rgb.copy()
segOv = rgb.copy()

mask = cv2.resize(mask, (new_N, new_M))




for i in range(new_M):
    for j in range(new_N):
        rM = mask[i,j,2]
        gM = mask[i,j,1]
        bM = mask[i,j,0]
        
        # if (rM==208) and (gM==1) and (bM==27):
        if ((rM>=190) and(rM<=220)) and (gM<=10) and ((bM>=15)and(bM<=40)):
            segP1[i,j,0] = rgb[i,j,0]
            segP1[i,j,1] = rgb[i,j,1]
            segP1[i,j,2] = 255

        # if (rM==245) and (gM==166) and (bM==37):
        #     segP2[i,j,0] = rgb[i,j,0]
        #     segP2[i,j,1] = 255
        #     segP2[i,j,2] = 255


allImage1 = np.hstack((rgb, mask, segP1))
# allImage2 = np.hstack((rgb, mask, segP2))

cv2.imshow("All Seg 1", allImage1)
# cv2.imshow("All Seg 2", allImage2)

cv2.waitKey(0)
cv2.destroyAllWindows()



