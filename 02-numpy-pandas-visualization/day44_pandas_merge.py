#Day 44:Pandas MErge ,Join and Contact

import pandas as pd

#Creating sample DataFrames
students = pd.DataFrame({
    "StudentID": [1,2,3,4,5],
    "Name":["Prachit","Asha","Riya","Sam","Tom"],
    "Age":[28,19,20,18,21]
})
marks = pd.DataFrame({
    "StudentID":[1,2,3,4,5],
    "Maths":[78,85,92,60,75],
    "Science":[82,79,88,55,72]
})

courses = pd.DataFrame({
    "StudentID":[1,2,3,4,5],
    "Course":["AI/ML","CS","IT","AI/ML","CS"],
    "City":["Mumbai","Delhi","Pune","Chennai","Bangalore"]
})

print("Students:\n",students)
print("\nMarks:\n",marks)
print("\nCourses:\n",courses)

#1.Inner merge - only matching rows
inner = pd.merge(students,marks,on="StudentID",how="inner")
print("\nInner merge:\n",inner)

#2.Left merge - all rows from left
left = pd.merge(students,marks,on="StudentID",how="left")
print("\nLeft merge:\n",left)

#3.Right merge - all rows from right
right = pd.merge(students,marks,on="StudentID",how="right")
print("\nRight merge:\n",right)

#4.Outer merge - all rows from both
outer = pd.merge(students,marks,on="StudentID",how="outer")
print("\nOuter merge:\n",outer)

#5.Merging 3 DataFrames
merged_all = pd.merge(students,marks,on="StudentID",how="inner")
merged_all = pd.merge(merged_all,courses,on="StudentID",how="inner")
print("\nAll 3 merged:\n",merged_all)

#6.concat()- stacking DataFrames
batch1 = pd.DataFrame({
    "Name":["Prachiti","Asha"],
    "Marks":[78,85]
})
batch2 = pd.DataFrame({
    "Name":["Riya","Sam"],
    "Marks":[92,60]
})

combined = pd.concat([batch1,batch2],ignore_index=True)
print("\nConcatenated:\n",combined)

#7.concat()horizontally
combined_h = pd.concat([students,courses.drop("StudentID",axis=1)],axis=1)
print("\nHorizontal concat:\n",combined_h)

#Mini Project:Student Complete Profile Builder
print("\n     STUDNET COMPLETE PROFILE     ")
complete = pd.merge(students,marks,on="StudentID",how="left")
complete = pd.merge(complete,courses,on="StudentID",how="left")
complete["Total"] = complete["Maths"] + complete["Science"]
complete["Average"] = complete["Total"] / 2
print(complete)
print("\nClass Average:",round(complete["Average"].mean(),2))