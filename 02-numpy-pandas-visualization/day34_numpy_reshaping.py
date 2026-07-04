#Day 34:Numpy Reshaping

import numpy as np

#1.reshape()
arr = np.arange(1,13)
print("Original:",arr)

reshaped = arr.reshape(3,4)
print("\nReshaped to (3,4):\n",reshaped)

reshaped2 = arr.reshape(4,3)
print("\nReshaped to (4,3):\n",reshaped2)

reshaped3 = arr.reshape(2,2,3)
print("\nReshaped to (2,2,3:\n)",reshaped3)

#2.flatten() - converts any array back to 1D
arr2d = np.array([[1,2,3],[4,5,6]])
flat = arr2d.flatten()
print("\nFlattened:",flat)

#3.ravel() - similar to flatten but returns aview
raveled = arr2d.ravel()
print("Raveled:",raveled)

#4.stack() - joining arrays
a = np.array([1,2,3])
b = np.array([4,5,6])

vstacked = np.vstack((a,b))
print("\nVertical stack:\n",vstacked)

hstacked = np.hstack((a,b))
print("Horizantal stack:",hstacked)

#5.split()- splitting arrays
arr3 = np.arange(1,10)
print("\nOriginal:",arr3)

split = np.split(arr3,3)
print("Split into 3:",split)

#6.resize()
arr4 = np.array([1,2,3,4])
resized = np.resize(arr4,(3,3))
print("\nResized to (3,3):\n",resized)

#Mini Project:Image Pixel Reshaper (simulated)
pixels = np.arange(1,25)
print("\n          IMAGE PIXEL RESHAPER      ")
print("Original pixels (1D):",pixels)

image = pixels.reshape(4,6)
print("\nAs 4x6 image:\n",image)

image2 = pixels.reshape(6,4)
print("\nAs 6x4 image:\n",image2)

flattened_back = image.flatten()
print("\nFlattened back to 1D:",flattened_back)