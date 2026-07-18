#Day 55:Combined Project - EDA on Real dataset (Part 1)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Step 1:Create realistic dataset
np.random.seed(42)
n = 100

data = {
    "StudentID":range(1,n + 1),
    "Name":["Student" + str(i) for i in range(1,n + 1)],
    "Age":np.random.randint(18,25,n),
    "Gender":np.random.choice(["Male","Female"],n),
    "City":np.random.choice(["Mumbai","Delhi","Pune","Chennai","Bangalore"],n),
    "Course":np.random.choice(["AI/ML","CS","IT","Data Science"],n),
    "Study_Hours":np.random.uniform(1,10,n).round(1),
    "Maths":np.random.randint(40,100,n),
    "Science":np.random.randint(40,100,n),
    "English":np.random.randint(40,100,n),
    "Computer":np.random.randint(40,100,n),
    "Attendance":np.random.randint(60,100,n)
}
df = pd.DataFrame(data)
df["Total"] = df["Maths"] + df["Science"] + df["English"] + df["Computer"]
df["Average"] = (df["Total"] / 4).round(2)
df["Grade"] = df["Average"].apply(lambda x:
     "A" if x>=90 else
     "B" if x>=75 else
     "C" if x>=60 else "D")
df["Result"] = df["Average"].apply(lambda x:
    "Pass" if x>=40 else "Fail")

print("Database Shape:",df.shape)
print("\nFirst 5 rows:\n",df.head())
print("\nDataset Info:")
df.info()

#Step 2:Basic EDA
print("\n     BASIC EDA       ")
print("\nStatistical Summary:\n",df.describe())
print("\nMissing Values:\n",df.isnull().sum())
print("\nGrade Distribution:\n",df["Grade"].value_counts())
print("\nCourse Distribution:\n",df["Course"].value_counts())
print("\nGender Distribution:\n",df["Gender"].value_counts())
print("\nCity Distribution:\n",df["City"].value_counts())

#Step 3:Univariate Analysis
fig,axes = plt.subplots(2,3,figsize=(15,10))
fig.suptitle("Univariate Analysis",fontsize=16)

#Age Distribution
sns.histplot(df["Age"],kde=True,ax=axes[0,0],color="blue")
axes[0,0].set_title("Age Distribution")

#Average marks Distribution
sns.histplot(df["Average"],kde=True,ax=axes[0,1],color="green")
axes[0,1].set_title("Average Marks Distribution")

#Study hours Distribution
sns.histplot(df["Study_Hours"],kde=True,ax=axes[0,2],color="orange")
axes[0,2].set_title("Study Hours Distribution")

#Grade Distribution
sns.countplot(x="Grade",data=df,palette="Set2",ax=axes[1,0])
axes[1,0].set_title("Grade Distribution")

#Course Distribution
sns.countplot(x="Course",data=df,palette="Set3",ax=axes[1,1])
axes[1,1].tick_params(axis="x",rotation=45)
axes[1,1].set_title("Course Distribution")

#Gender Distribution
sns.countplot(x="Gender",data=df,palette="pastel",ax=axes[1,2])
axes[1,2].set_title("Gender Distribution")

plt.tight_layout()
plt.savefig("day55_univariate.png")
plt.show()
print("Univariate analysis saved")

#Step 4:Subject-wise Analysis
print("\n      SUBJECT ANALYSIS  ")
subjects = ["Maths","Science","English","Computer"]
for sub in subjects:
    print(sub, "-Mean",round(df[sub].mean(),2),
          "| Std:",round(df[sub].std(),2),
          "| Min:",df[sub].min(),
          "| Max:",df[sub].max())

#Step 5:Saved dataset or next parts
df.to_csv("eda_dataset.csv",index=False)
print("\nDataset saved as eda_dataset.csv for next parts")