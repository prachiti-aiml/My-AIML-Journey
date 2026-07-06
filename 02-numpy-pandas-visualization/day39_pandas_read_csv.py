#Day 39:Pandas Read CSV

import pandas as pd
import numpy as np

#First create a sample CSV file to work with
sample_data = {
    "Name": ["Prachiti","Asha","Riya","Sam","Tom","Neha","Raj","Priya"],
    "Age": [18,19,20,18,21,19,22,20],
    "Marks":[78,89,92,60,75,88,45,95],
    "City":["Mumbai","Delhi","Pune","Chennai","Bangalore","Mumbai","Delhi","Pune"],
    "Course":["AI/ML","CS","IT","AI/ML","CS","IT","AI/Ml","CS"]
}

df_sample = pd.DataFrame(sample_data)
df_sample.to_csv("students.csv",index=False)
print("Sample CSV created:students.csv")

#1.Reading a CSV File
df = pd.read_csv("students.csv")
print("\nDataFrame from CSV:\n",df)

#2.Basic info
print("\nShape:",df.shape)
print("Columns:",df.columns.tolist())

#3.First and last rows
print("\nFirst 3 rows:\n",df.head(3))
print("\nLast 3 rows:\n",df.tail(3))

#4.Basic statistics
print("\ndescribe:\n",df.describe())

#5.Checking for missing values
print("\nMissing values:\n",df.isnull().sum())

#6.Selecting specific columns
print("\nName and Marks only:\n",df[["Name","Marks"]])

#7.Filtering rows
print("\nstudents from Mumbai:\n",df[df["City"] == "Mumbai"])
print("\nStudents with marks above 80:\n",df[df["Marks"] > 80])

#8.Saving filtered data to new CSV
top_students = df[df["Marks"] >= 80] 
top_students.to_csv("top_students.csv",index=False) 
print("\nTop students saved to top_students.csv")

#Mini Project:Student Data Analyzer from CSV
print("\n     STUDENT DATA ANALYZER      ")
print("Total students:",len(df))
print("Average marks:",round(df["Marks"].mean(),2))
print("Highest marks:",df["Marks"].max(),"-",df.loc[df["Marks"].idxmax(),"Name"])
print("Lowest marks:",df["Marks"].min(),"-",df.loc[df["Marks"].idxmin(),"Name"])
print("\nStudents per city:\n",df["City"].value_counts())
print("\nStudents per course:\n",df["Course"].value_counts())