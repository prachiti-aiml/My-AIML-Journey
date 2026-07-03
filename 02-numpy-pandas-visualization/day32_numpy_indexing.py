#Day 32 : NumPy Indexing and Slicing

import numpy as np


#1.Indexing in 1D Array
arr = np.array([10,20,30,40,50])
print("Array:",arr)
print("First Element:",arr[0])
print("Last Element:",arr[-1])
print("Third Element:",arr[2])

#2.Slicing in 1D Array
print("\nSlice [1:4]",arr[1:4])
print("Slice [:3]:",arr[:3])
print("Slice [2:]:",arr[2:])
print("Reverse:",arr[::-1])

#3.Indexing in 2D Array
arr2d = np.array([[1,2,3],[4,5,6],[7,8,9]])
print("\n2D Array:\n",arr2d)
print("Element at row 0,col 1:",arr2d[0,1])
print("Element at row 2,col 2:",arr2d[2,2])

#4.Slicing in 2D Array
print("\nFirst row:",arr2d[0])
print("First Column:",arr2d[:,0])
print("Last Column:",arr2d[:,-1])
print("Sub matrix (rows 0-1,cols 1-2):\n",arr2d[0:2,1:3])

#5.Boolean Indexing
marks = np.array([45,78,92,33,67,88,55,21,99,60])
print("\nMarks above 70:",marks[marks > 70])
print("Marks below 50:",marks[marks < 50])

#6.Fancy Indexing
arr3 = np.array([10,20,30,40,50])
indices = [0,2,4]
print("\nFancy indexing [0,2,4]:",arr3[indices])

#Mini Project:Student Marks Selector
students = np.array(["Asha","Riya","Sam","Tom","Neha"])
marks = np.array([78,45,92,33,67])

print("\n     STUDENT MARKS SELECTOR      ")
print("All students:",students)
print("All marks:",marks)

passed = students[marks >= 40]
failed = students[marks < 40]
top_students = students[marks >= 80]

print("Passed students:",passed)
print("Failed students:",failed)
print("Top students (>=80):",top_students)