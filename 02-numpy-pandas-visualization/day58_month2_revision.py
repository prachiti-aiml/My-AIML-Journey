#Day 58:Month 2 Revision -Polish and Push Full Project
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Step 1:Load or create final dataset
np.random.seed(42)
n = 100

data={
    "Student ID": range(1,n + 1),
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
    "A" if x >= 90 else
    "B" if x >= 75 else
    "C" if x >= 60 else "D")
df["Result"] = df["Average"].apply(lambda x:
    "Pass" if x>= 40 else "Fail")

print("Dataset Shape:",df.shape)
print("\nFirst 5 rows:\n",df.head())

#Step 2:Data Cleaning Summary
print("\n    DATA QUALITY CHECK    ")
print("Missing values:\n",df.isnull().sum())
print("Duplicates:",df.duplicated().sum())
print("Data Types:\n",df.dtypes)

#Step 3:Statistical Summary
print("\n   STATISTICAL SUMMARY     ")
print(df.describe().round(2))

#Step 4:Key Metrics
print("\n    KEY METRCIS ")
print("Total students:",len(df))
print("Pass rate:",round((df["Result"] == "Pass").sum() / len(df) * 100,2),"%")
print("Overall Average:",round(df["Average"].mean(),2))
print("Top Course:",df.groupby("Course")["Average"].mean().idxmax())
print("Top city:",df.groupby("City")["Average"].mean().idxmax())

subjects = ["Maths","Science","English","Computer"]
print("\nSubject averages:")
for s in subjects:
    print(" ",s,":",round(df[s].mean(),2))

#Step 5:Final Polished Dashboard
fig = plt.figure(figsize=(18,12))
fig.suptitle("Month 2 Final Project - Student Performance Report",fontsize=18,fontweight="bold")

#Plot 1:Grade Distribution
ax1 = fig.add_subplot(2,4,1)
grade_counts = df["Grade"].value_counts()
ax1.pie(grade_counts,labels=grade_counts.index,
        autopct="%1.1f%%",
        colors=["gold","lightblue","lightgreen","salmon"])
ax1.set_title("Grade Distribution")

#Plot 2:Average Marks by Course
ax2 = fig.add_subplot(2,4,2)
course_avg = df.groupby("Course")["Average"].mean().round(2)
ax2.bar(course_avg.index,course_avg.values,color=["blue","green","orange","red"])
ax2.set_title("Avg Marks by Course")
ax2.tick_params(axis="x",rotation=45)
ax2.set_ylabel("Average")

#Plot 3:Study Hours vs Marks
ax3 = fig.add_subplot(2,4,3)
ax3.scatter(df["Study_Hours"],df["Average"],c=df["Average"],cmap="viridis",alpha=0.6,s=50)
ax3.set_title("Study Hours vs Marks")
ax3.set_xlabel("Study Hours")
ax3.set_ylabel("Average")
ax3.grid(True)

#Plot 4:Gender Distribution
ax4 = fig.add_subplot(2,4,4)
gender_counts = df["Gender"].value_counts()
ax4.pie(gender_counts,labels=gender_counts.index,autopct="%1.1f%%",colors=["lightblue","pink"])
ax4.set_title("Gender Distribution")

#Plot 5:Marks Distribution
ax5 = fig.add_subplot(2,4,5)
ax5.hist(df["Average"],bins=15,color="purple",edgecolor="black",alpha=0.7)
ax5.set_title("Marks Distribution")
ax5.set_xlabel("Average Marks")
ax5.set_ylabel("Frequency")
ax5.grid(True)

#Plot 6:Subject Comparison
ax6 = fig.add_subplot(2,4,6)
subject_means = [df[s].mean() for s in subjects]
bars = ax6.bar(subjects,subject_means,color=["blue","green","orange","red"],edgecolor="black")
ax6.set_title("Subject Averages")
ax6.set_ylabel("Average Marks")
for bar,val in zip(bars,subject_means):
    ax6.text(bar.get_x( ) + bar.get_width()/2,
             bar.get_height()+0.5,
             str(round(val,1)),ha="center",fontsize=9)

#Plot 7:Attendance vs Marks
ax7 = fig.add_subplot(2,4,7)
ax7.scatter(df["Attendance"],df["Average"],alpha=0.6,color="teal",s=50)
ax7.set_title("Attendance vs Marks")
ax7.set_xlabel("Attendance %")
ax7.set_ylabel("Average Marks")
ax7.grid(True)

#Plot 8:Correlation Heatmap
ax8 = fig.add_subplot(2,4,8)
corr = df[["Maths","Science","English","Computer","Average"]].corr()
sns.heatmap(corr,annot=True,fmt=".1f",cmap="coolwarm",ax=ax8,linewidths=0.5,annot_kws={"size":7})
ax8.set_title("Correlation Heatmap")

plt.tight_layout()
plt.savefig("day58_final_dashboard.png")
plt.show()
print("\nFinal dahsboard saved as day58_final_dashboard.png")

#Step 6:save Final Report
df.to_csv("month2_final_report.csv",index=False)
print("Final report saved as month2_final_report.csv")

print("\n    MONTH 2 COMPLETE   ")
print("Numpy,Pandas and Visualization-Done!")
print("Next:Phase 3 - Statistics for ML")