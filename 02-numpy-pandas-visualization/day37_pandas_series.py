#Day 37:Pandas Series

import pandas as pd
import numpy as np

#1.Creating a series
s1 = pd.Series([10,20,30,40,50])
print("Basic Series:\n",s1)

#2.Series with custom index
s2 = pd.Series([78,85,92,60,75],
              index = ["Maths","Science","English","History","Computer"])
print("\nSeries with custom index:\n",s2)

#3.Accessing elements
print("\nMaths marks:",s2["Maths"])
print("First element:",s2.iloc[0])
print("Last element:",s2.iloc[-1])

#4.Slicing a Series
print("\nFirst 3 subjects:\n",s2.iloc[:3])
print("Subjects above 80:\n",s2[s2 > 80])

#5.Series operations
print("\nAdd 5 to all marks:\n",s2 + 5)
print("Multiply by 2:\n",s2 * 2)

#6.Series from Dictionary
data = {"name":"Prachiti","age":18,"college":"VPCOE","year":1}
s3 = pd.Series(data)
print("\nSeries from dictionary:\n",s3)

#7.Series statistics
marks = pd.Series([45,78,92,33,67,88,55,21,99,60])
print("\nMarks Series statistics:")
print("Mean:",marks.mean())
print("Median:",marks.median())
print("Std:",marks.std())
print("Max:",marks.max())
print("Min:",marks.min())
print("Sum:",marks.sum())
print("\nDescribe:\n",marks.describe())

#Mini Project:Student Subject Tracker
subjects = ["Maths","Science","English","History","Computer"]
marks = pd.Series([78,85,62,90,95],index=subjects)

print("\n       STUDENT SUBJECT TRACKER           ")
print("All marks:\n",marks)
print("\nAverage:",marks.mean())
print("Highest:",marks.max(),"in",marks.idxmax())
print("Lowest:",marks.min(),"in",marks.idxmin())
print("\nSubjects passed (>=40):\n",marks[marks >= 40])
print("Subjects failed (<40):\n",marks[marks < 40])