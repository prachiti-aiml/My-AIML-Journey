#Day 46:Pandas Apply and Map
import pandas as pd
import numpy as np

#Creating sample DataFrame
data = {
    "Name":["Prachiti","Asha","Riya","Sam","Tom","Neha","Raj","Priya"],
    "Marks":[78,85,92,60,75,88,45,95],
    "Age":[18,19,20,18,21,19,22,20],
    "City":["Mumbai","Delhi","Pune","Chennai","Bangalore","Mumbai","Delhi","PUne"]
}
df = pd.DataFrame(data)
print("DataFrame:\n",df)

#1.apply() on a column
def get_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 60:
        return "C"
    else:
        return "D"
    
df["Grade"] = df["Marks"].apply(get_grade)
print("\nWith Grade Column :\n",df)

#2.apply() with lambda
df["Marks_plus5"] = df["Marks"].apply(lambda x: x + 5)
print("\nMarks + 5 bonus:\n",df[["Name","Marks","Marks_plus5"]])

#3.apply()on multiple columns (axis=1)
df["Name_City"] = df.apply(lambda row: row["Name"] + "-" + row["City"],axis=1)
print("\nName and City combined:\n",df[["Name","City","Name_City"]])

#4.map() on a series
city_map = {
    "Mumbai":"Maharashtra",
    "Delhi":"Delhi",
    "Pune":"Maharashtra",
    "Chennai":"Tamil Nadu",
    "Bangalore":"Karnataka"
}
df["State"] = df["City"].map(city_map)
print("\nWith State column:\n",df[["Name","City","State"]])

#5.applymap() on entire DataFrame (now called map in newer pandas)
marks_df = pd.DataFrame({
    "Maths":[78,85,92],
    "Science":[82,79,88],
    "English":[70,90,75]
})
rounded = marks_df.apply(lambda x:x.round(0))
print("\nRounded marks:\n",rounded)

#6.apply()for row-wise calculation
df["Total"] = df[["Marks"]].apply(lambda x: x* 2,axis = 0)
print("\nDouble marks:\n",df[["Name","Marks","Total"]])

#Mini Project:Employee Salary Calculator
employees = pd.DataFrame({
    "Name":["Asha","Riya","Sam","Tom","Neha"],
    "Department":["AI","HR","AI","Finance","HR"],
    "Base_Salary":[30000,25000,35000,28000,27000],
    "Experience":[2,1,3,2,1]
})

def calculate_bonus(row):
    if row["Department"] == "AI":
        return row["Base_Salary"] * 0.20
    elif row["Department"] == "HR":
        return row["Base_Salary"] * 0.10
    else:
        return row["Base_Salary"] * 0.15
    
employees["Bonus"] = employees.apply(calculate_bonus,axis=1)
employees["Total_Salary"] = employees["Base_Salary"] + employees["Bonus"]
employees["Level"] = employees["Experience"].map({1: "Junior",2: "Mid",3: "Senior"})
    
print("\n  EMPLOYEE SALARY CALCULATOR     ")
print(employees)
print("\nTotal salary expense:",employees["Total_Salary"].sum())