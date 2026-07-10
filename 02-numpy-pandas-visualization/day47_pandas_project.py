#Day 47:Pandas Project:Clean a Real Dataset

import pandas as pd
import numpy as np

#Step 1:Create a messy dataset (simulating real world data)
messy_data = {
    "Name":["Prachiti","Asha","Riya","Sam","Tom","Neha",None,"Priya"],
    "Age":[18,19,200,18,21,None,19,20],
    "Marks":[78,85,92,None,75,88,45,95],
    "City":["Mumbai","Delhi","Pune","Chennai","Bangalore","Mumbai","Delhi",None],
    "Email":["p@gmail.com","asha@gmail.com","riya@yahoo","sam@gmail.com","tom@gmail.com","neha@gmail.com","raj@gmail.com","priya@gmail.com"],
    "Phone":["9876543210","123","9123456780","9988776655","9876543211","9123456781","99887","9876543212"]
}
df = pd.DataFrame(messy_data)
print("MESSY DATASET:")
print(df)
print("\nShape:",df.shape)
print("\nMissing values:\n",df.isnull().sum())

#Step 2:Fix Name Formatting
df["Name"] = df["Name"].str.title()
print("\nAfter fixing names:\n",df["Name"])

#Step 3:Fix City Formatting
df["City"] =df["City"].str.title()
print("After fixing cities:\n",df["City"])

#Step 4:Handle Missing Values
df["Name"] = df["Name"].fillna("Unknown")
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())
df["City"] = df["City"].fillna("Unknown")

#Step 5:Fix invalid ages (age>100 is invalid)
df["Age"] = df["Age"].apply(lambda x:df["Age"].median() if x >100 else x)
print("\nAfter Fixing invalid ages:\n",df["Age"])

#Step 6: Validate email addresses
def is_valid_email(email):
    return "@" in str(email) and "." in str(email).split("@")[-1]

df["Email_Valid"] = df["Email"].apply(is_valid_email)
print("\nEmail validaiton:\n",df[["Email","Email_Valid"]])

#Step 7:Validate phone numbers
def is_valid_phone(phone):
    return len(str(phone)) == 10 and str(phone).isdigit()

df["Phone_Valid"] = df["Phone"].apply(is_valid_phone)
print("\nPhone validation:\n",df[["Phone","Phone_Valid"]])

#Step 8:Grade column
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

#Step 9:Final clean dataset
print("\nFINAL CLEAN DATASET:")
print(df)
print("\nMissing values after cleaning:\n",df.isnull().sum())

#Step 10:Save cleaned data
df.to_csv("cleaned_data_csv",index=False)
print("\nCleaned data saved to cleaned_data_csv")

#Step 11:Summary Report
print("\n    CLEANING SUMMARY   ")
print("Total records:",len(df))
print("Valid emails:",df["Email_Valid"].sum())
print("Invalid emails:",(~df["Email_Valid"]).sum())
print("Valid phones:",df["Phone_Valid"].sum())
print("Invalid phones:",(~df["Phone_Valid"]).sum())
print("Average marks:",round(df["Marks"].mean(),2))
print("Grade Distribution:\n",df["Grade"].value_counts())