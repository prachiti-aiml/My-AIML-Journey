#Day 38:Pandas Dataframe

import pandas as pd
import numpy as np

#1.Creating a Dataframe
data = {
    "Name":["Prachiti","Asha","Riya","Sam","Tom"],
    "Age":[18,19,20,18,21],
    "Marks":[78,85,92,60,75],
    "City":["Mumbai","Delhi","Pune","Chennai","Bangalore"]
}

df = pd.DataFrame(data)
print("DataFrame:\n",df)

#2.Basic info
print("\nShape:",df.shape)
print("Columns:",df.columns.tolist())
print("Data types:\n",df.dtypes)
print("\nInfo:")
df.info()

#3.Accessing columns
print("\nNames column:\n",df["Name"])
print("\nMarks column:\n",df["Marks"])

#4.Accessing rows
print("\nFirst row:\n",df.iloc[0])
print("\nFirst 3 rows:\n",df.head(3))
print("\nLast 2 rowws:\n",df.tail(2))

#5.Accessing specific cell
print("\nMarks of Riya:",df.iloc[2]["Marks"])

#6.Adding a new column
df["Grade"]= ["B","B","A","C","B"]
print("\nWith Grade Column:\n",df)

#7.Dropping a column
df2 = df.drop("City",axis=1)
print("\nAfter dropping City:\n",df2)

#8.Basic statistics
print("\nDescribe:\n",df["Marks"].describe())

#Mini Project:Student Report Card Dataframes 
students = {
    "Name":["Prachit","Asha","Riya","Sam","Tom"],
    "Maths":[78,85,92,45,67],
    "Science":[82,79,88,55,72],
    "English":[70,90,75,60,80]
}
report = pd.DataFrame(students)
report["Total"] = report["Maths"] + report["Science"] + report["English"]
report["Average"] = report["Total"] / 3
report["Result"] = report["Average"].apply(lambda x:"Pass" if x>= 40 else "Fail")

print("\n       STUDENT REPORT CARD      ")
print(report)
print("\nClass average:",round(report["Average"].mean(),2))
print("Topper:",report.loc[report["Average"].idxmax(),"Name"])