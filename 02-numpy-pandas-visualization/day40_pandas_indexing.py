#Day 40:Pandas Indexing - loc and iloc
import pandas as pd

#Creating sample DataFrame
data = {
    "Name":["Prachiti","Asha","Riya","Sam","Tom"],
    "Age":[18,19,20,18,21],
    "Maths":[78,85,92,60,75],
    "Science":[82,79,88,55,72],
    "English":[70,90,75,60,80]
}
df = pd.DataFrame(data)
print("DayaFrame:\n",df)

#1.iloc - index based (uses numbers)
print("\n    iloc    ")
print("First row:\n",df.iloc[0])
print("\nFirst 3 rows:\n",df.iloc[:3])
print("\nRow 1 to 3:\n",df.iloc[1:4])
print("\nSpecific cell (row 2,col 3):",df.iloc[2,3])
print("\nFirst 3 rows,first 3 cols:\n",df.iloc[:3,:3])

#2.loc - label based (uses column names)
print("\n   loc   ")
print("First row by label:\n",df.loc[0])
print("\nName and Maths columns:\n",df.loc[:,["Name","Maths"]])
print("\nRows 0-2,Name and Science:\n",df.loc[0:2,["Name","Science"]])

#3.Setting custom index
df2 = df.set_index("Name")
print("\nDataFrame with Name as index:\n",df)
print("\nPrachiti's data:\n",df2.loc["Prachiti"])
print("\nAsha's Maths:",df2.loc["Asha","Maths"])

#4.Resetting index
df3 = df2.reset_index()
print("\nAfter reset index:\n",df3)

#5.Conditional selection with loc
print("\nStudents with Maths > 80:\n",df.loc[df["Maths"] > 80])
print("\nName and Maths where Science > 80:\n",
      df.loc[df["Science"] > 80,["Name","Science"]])

#Mini Project:Score Lookup System
print("\n      SCORE LOOKUP SYSTEM      ")
df_indexed = df.set_index("Name")

student = input("Enter student name to look up:")
if student in df_indexed.index:
    print("\nDetails for",student,":")
else:
    print("Student not found.")