import cv2
import os
import numpy as np

# set the paths
rgbPath = r"C:\Users\Esa\Pictures\_DATASET\Plank30\kFoldFolders\D3\Thalassiosira sp (large) (400X) PariIslandRisetPro19 St10_FDpXsbOPwA\images\Thalassiosira sp (large) (400X) PariIslandRisetPro19 St10_FDpXsbOPwA.jpg"
bwPath = r"C:\Users\Esa\Pictures\_DATASET\Plank30\result0\Thalassiosira sp (large) (400X) PariIslandRisetPro19 St10_FDpXsbOPwA.jpg"


# rgbPath = r"C:\Users\Esa\Pictures\_DATASET\Plank30\kFoldFolders\D3\Chaetoceros laciniosus (200X) PariIslandRisetPro2019 St10\images\Chaetoceros laciniosus (200X) PariIslandRisetPro2019 St10.jpg"
# bwPath = r"C:\Users\Esa\Pictures\_DATASET\Plank30\result0\Chaetoceros laciniosus (200X) PariIslandRisetPro2019 St10.jpg"



rgb = cv2.imread(rgbPath)
bw = cv2.imread(bwPath)

M = bw.shape[0]
N = bw.shape[1]

seg = np.zeros((M, N, 3), np.uint8)

for i in range(M):
    for j in range(N):
        if bw[i,j,0] == 255:
            for k in range(3):
                seg[i,j,k] = rgb[i,j,k]

#cv2.imshow("rgb", rgb)
#cv2.imshow("bw", bw)
cv2.imshow("SEG", seg)



cv2.waitKey(0)
cv2.destroyAllWindows()
