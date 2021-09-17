import os
import numpy as np 
import shutil


os.system("cls")

imgIdx = []
for i in range(10):
	imgIdx.append(i)

print(imgIdx)

# Get all permutations of [1, 2, 3]


idxFiles = np.random.permutation(360)
print(idxFiles)




imgPath = r"C:\Users\Esa\Pictures\_DATASET\Plank30\img"
bwPath = r"C:\Users\Esa\Pictures\_DATASET\Plank30\bw"


imgFiles = os.listdir(imgPath)

NFiles = len(imgFiles)
#for i in range(NFiles):
#	print("%d %s  "%(i,imgFiles[i]))





tarPath = r"C:\Users\Esa\Pictures\_DATASET\Plank30\kFoldFolders"
DName = ["D0", "D1", "D2", "D3"] 

i = 0
for fold in range(4):
	print(" ")
	for i0 in range(0,90,1):
		rootFolder = os.path.join(tarPath,DName[fold],imgFiles[idxFiles[i]][:-4])
		rootFoldPath = os.path.join(rootFolder)
		print("Fold %d   %d   %s    %d -----> %s"%(fold,i,DName[fold], idxFiles[i], rootFoldPath))
		if not os.path.exists(rootFoldPath):
			os.mkdir(rootFoldPath)
			imgFoldPath = os.path.join(rootFoldPath,"images")
			os.mkdir(imgFoldPath)
			print("Fold %d   %d   %s    %d -----> %s"%(fold,i,DName[fold], idxFiles[i], imgFoldPath))

			oriPath = os.path.join(imgPath,imgFiles[idxFiles[i]])
			newPath = os.path.join(imgFoldPath,imgFiles[idxFiles[i]])
			print(oriPath)
			print(newPath)
			shutil.copyfile(oriPath, newPath)
			


			maskFoldPath = os.path.join(rootFoldPath,"mask")
			os.mkdir(maskFoldPath)
			print("Fold %d   %d   %s    %d -----> %s"%(fold,i,DName[fold], idxFiles[i], maskFoldPath))
			oriPath = os.path.join(bwPath,imgFiles[idxFiles[i]])
			newPath = os.path.join(maskFoldPath,imgFiles[idxFiles[i]])
			print(oriPath)
			print(newPath)
			shutil.copyfile(oriPath, newPath)
		i = i + 1

		print("--")
