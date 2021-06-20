import numpy as np 
import json
import os
import cv2

os.system("cls")


path0 = r"C:\Users\Esa\Pictures\_DATASET\Augmented_2\Augmented_2\Plank30"


jsonPath = os.path.join(path0,"ann")
bwPath  =  os.path.join(path0,"bw")
rgbPath =  os.path.join(path0,"img")

print(jsonPath)
print(bwPath)
print(rgbPath)

rgbFiles = os.listdir(rgbPath)
img0 = cv2.imread(os.path.join(rgbPath,rgbFiles[5]))
M = img0.shape[0]
N = img0.shape[1]

jsonFiles = os.listdir(jsonPath)

idxF = 0
for jF in jsonFiles:
#for idxF in range(1,60,1):

	imgFileName = rgbFiles[idxF]
	img0 = cv2.imread(os.path.join(rgbPath,imgFileName))
	M = img0.shape[0]
	N = img0.shape[1]


	jF = imgFileName+".json"##jsonFiles[idxF]
	print(jF)

	with open(os.path.join(jsonPath,jF)) as json_file:
		data = json.load(json_file)

	NoOfObj = len(data['objects'])

	bwImg = np.zeros((M, N, 3), np.uint8)

	for kObj in range(1,NoOfObj,1):
		pcs = data['objects'][kObj]['points']['exterior']
		print(pcs)

		#bwImg = np.zeros((M, N, 3), np.uint8)
		polygon = np.array(pcs).astype('int32')

		print(polygon)

		#cv2.fillConvexPoly(bwImg, polygon, (255,255,255))

		#isClosed = True
		#color = (255, 255, 255)
		#thickness = 3
		#bwImg = cv2.polylines(bwImg, [polygon],isClosed, color,thickness)
		cv2.fillPoly(bwImg, pts = [polygon], color =(255,255,255))

	#cv2.imshow(str(idxF),bwImg)
	

	cv2.imwrite((os.path.join(bwPath,jF[:-5])),bwImg)
	idxF = idxF + 1



print("Final index is %d "%(idxF))
cv2.waitKey(0)
cv2.destroyAllWindows()

