#Day 33:Numpy Operators

import numpy as np

#1.Basic arithmetic operations
a = np.array([1,2,3,4,5])
b = np.array([10,20,30,40,50])

print("a:",a)
print("b:",b)
print("a + b:",a + b)
print("a - b:",a - b)
print("a * b:",a * b)
print("a / b:",a / b)
print("a ** 2:",a ** 2)

#2.Broadcasting
arr = np.array([1,2,3,4,5])
print("\nOriginal:",arr)
print("Add 100:",arr + 100)
print("Multiply by 5:",arr * 5)

#3.Math functions
print("\nSquare root:",np.sqrt(a))
print("Absolute value:",np.abs(np.array([-1,-2,3,-4,5])))
print("Exponential:",np.exp(a))
print("Log:",np.log(b))

#4.Aggregate functions
marks = np.array([45,78,92,33,67,88,55,21,99,60])
print("\nMarks:",marks)
print("Sum:",np.sum(marks))
print("Mean:",np.mean(marks))
print("Median:",np.median(marks))
print("Std deviation:",np.std(marks))
print("Variance:",np.var(marks))
print("Min:",np.min(marks))
print("Max:",np.max(marks))

#5.Matrix Operation
mat1 = np.array([[1, 2],[3, 4]])
mat2 = np.array([[5, 6],[7, 8]])

print("\nMatrix 1:\n",mat1)
print("Matrix 2:\n",mat2)
print("Matrix addition:\n",mat1 + mat2)
print("Matrix multiplication:\n",np.dot(mat1,mat2))
print("Transpose of mat1:\n",mat1.T)

#Mini Project:Sales Data Analyzer
sales = np.array([15000,22000,18000,30000,25000,28000,20000])
days = np.array(["Mon","Tue","Wed","Thu","Fri","Sat","Sun"])

print("\n       SALES DATA ANALYZER           ")
print("Daily sales:",sales)
print("Total sales:",np.sum(sales))
print("Average sales:",np.mean(sales))
print("Highest sales:",np.max(sales),"on",days[np.argmax(sales)])
print("Lowest sales:",np.min(sales),"on",days[np.argmin(sales)])
print("Days above average:",days[sales > np.mean(sales)])