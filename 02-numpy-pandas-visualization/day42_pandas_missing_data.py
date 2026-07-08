#Day 42:Pandas Missing Data

import pandas as pd
import numpy as np

#Creating DataFrame with missing values
data = {
    "Name": ["Prachiti","Asha","Riya","Sam","Tom","Neha"],
    "Age":[18,19,None,18,21,19],
    "Marks":[78,None,92,60,None,88],
    "City":["Mumbai","Delhi",None,"Chennai","Bangalore",None],
    "Course": ["AI/ML","CS","IT",None,"CS","IT"]
}
df = pd.DataFrame(data)
print("DataFrame with missing values:\n",df)

#1.Checking Missing values
print("\nMissing values per column:\n",df.isnull().sum())
print("\nTotal missing values:",df.isnull().sum().sum())
print("\nMissing value percentage:\n",
      round(df.isnull().sum() / len(df) * 100,2))

#2.dropna() - dropping rows with missing values
df_dropped = df.dropna()
print("\nAfter dropping rows with NaN:\n",df_dropped)

#3.dropna() with threshold
df_thresh = df.dropna(thresh=4)
print("\nAfter dropna with thresh=4:\n",df_thresh)

#4.fillna() - filling missing values
df_filled = df.copy()
df_filled["Age"] = df_filled["Age"].fillna(df_filled["Age"].mean())
df_filled["Marks"] = df_filled["Marks"].fillna(df_filled["Marks"].median())
df_filled["City"] = df_filled["City"].fillna("Unknown")
df_filled["Course"] = df_filled["Course"].fillna("Not specified")
print("\nAfter filling missing values:\n",df_filled)

#5.Forward fill and backward fill
df_ffill = df.fillna(method="ffill")
print("\nForward fill:\n",df_ffill)

#6.Replacing specific values
df_replaced = df.replace(np.nan,"Missing")
print("\nAfter replacing NaN with 'Missing':\n",df_replaced)

#Mini Project:Data Cleaner
print("\n     DATA CLEANER    ")
print("Original data missing values:\n",df.isnull().sum())

clean_df = df.copy()
clean_df["Age"] = clean_df["Age"].fillna(clean_df["Age"].mean())
clean_df["Marks"] = clean_df["Marks"].fillna(clean_df["Marks"].mean())
clean_df["City"] = clean_df["City"].fillna("Unknown")
clean_df["Course"] = clean_df["Course"].fillna("Not specified")

print("\nCleaned data:\n",clean_df)
print("\nMissing values after cleaning:\n",clean_df.isnull().sum())

clean_df.to_csv("cleaned_students.csv",index=False)
print("\nCleaned data saved to cleaned_students.csv")
