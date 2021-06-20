import numpy as np 
import json
import os
import cv2



path = r"C:\Users\Esa\Pictures\_DATASET\Augmented_2\Augmented_2\Plank30\ann"

'''
y = os.listdir(path)
N = len(y)
for i in range(N):
	if y[i].endswith(".jpg.j"):
		oldFile = os.path.join(path,y[i])
		newFile = oldFile+".son"
		print("\n")
		print(oldFile)
		print(newFile)
		os.rename(oldFile,newFile)
'''

'''
y = os.listdir(path)
N = len(y)
for i in range(N):
	oldFile = os.path.join(path,y[i])
	newFile = oldFile+".json"
	print("\n")
	print(oldFile)
	print(newFile)
	os.rename(oldFile,newFile)
'''


y = os.listdir(path)
N = len(y)
idx = 1
for i in range(N):
	if y[i].endswith(".json"):
		oldFile = os.path.join(path,y[i])
		newFile = oldFile[:-5]
		newFile = newFile+".jpg.json"
		print("%d "%(idx))
		print(oldFile)
		print(newFile)
		print(" ")
		idx = idx + 1
		os.rename(oldFile,newFile)

