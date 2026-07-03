#Day 31:Numpy Introduction
import numpy as np

#1.Creating arrays
arr1 = np.array([1,2,3,4,5])
print("1D Array:",arr1)

arr2 = np.array([[1,2,3],[4,5,6]])
print("2D Array:\n",arr2)

#2.Array properties
print("\nShape:",arr1.shape)
print("Shape of 2D:",arr2.shape)
print("Data type:",arr1.dtype)
print("Size:",arr1.size)
print("Dimensions:",arr2.ndim)

#3.Special arrays
zeros = np.zeros((3,3))
print("\nZeros array:\n",zeros)

ones = np.ones((2,4))
print("Ones array:\n",ones)

identity = np.eye(3)
print("Identity matrix:\n",identity)

#4.Array with range
range_arr = np.arange(0,20,2)
print("\nArange:",range_arr)

linspace_arr = np.linspace(0,1,5)
print("Linspace:",linspace_arr)

#5.Basic math on arrays
a = np.array([1,2,3,4,5])
print("\nOriginal:",a)
print("Add 10:",a + 10)
print("Multiply by 2:",a * 2)
print("Square:",a**2)

#Mini Project:Students Marks Analysis using Numpy
marks = np.array([45,78,92,33,67,88,55,21,99,60])

print("\n       MARKS ANALYSIS         ")
print("Marks:",marks)
print("Highest:",np.max(marks))
print("Lowest:",np.min(marks))
print("Average:",np.mean(marks))
print("Total:",np.sum(marks))
print("Passed (>=40):",marks[marks >=40])
print("Failed (<40):",marks[marks < 40])