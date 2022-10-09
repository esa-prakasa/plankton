import numpy as np 
import json
import os
import cv2

os.system("cls")

// loading file

jsonPath = r"C:\Users\Esa\Documents\___KEGIATAN-Ku 2021\01.21 -- Plankto IPK\IPB Conf 2021\Figures\Thalassionema nitzschioides-2 (200X) PariIslandRisetPro2019 St10.jpg.json"
rgbPath = r"C:\Users\Esa\Documents\___KEGIATAN-Ku 2021\01.21 -- Plankto IPK\IPB Conf 2021\Figures\PlanktonSegmentation_Plank30_Thalassionema nitzschioides-2 (200X) PariIslandRisetPro2019 St10.jpg"

print(jsonPath)
print(rgbPath)

img0 = cv2.imread(rgbPath)
M = img0.shape[0]
N = img0.shape[1]

with open(jsonPath) as json_file:
	data = json.load(json_file)

NoOfObj = len(data['objects'])
print(NoOfObj)

bwImg = np.zeros((M, N, 3), np.uint8)

pcs = data['objects'][0]['points']['exterior']
print(pcs)
    
polygon = np.array(pcs).astype('int32')
cv2.fillPoly(bwImg, pts = [polygon], color =(255,255,255))

cv2.imshow("RGB",img0)
cv2.imshow("BW",bwImg)

#cv2.imwrite((os.path.join(bwPath,jF[:-5])),bwImg)


cv2.waitKey(0)
cv2.destroyAllWindows()

