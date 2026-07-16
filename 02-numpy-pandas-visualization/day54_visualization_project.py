#Day 54:Visualization Project - Cleaned Dataset Analysis
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Step 1:Create and clean dataset
np.random.seed(42)
data = {
    "Name": ["Student" + str(i) for i in range(1,31)],
    "Age": np.random.randint(18,25,30),
    "Maths": np.random.randint(40,100,30),
    "Science": np.random.randint(40,100,30),
    "English": np.random.randint(40,100,30),
    "Computer": np.random.randint(40,100,30),
    "City": np.random.choice(["Mumbai","Delhi","Pune","Chennai"],30),
    "Course": np.random.choice(["AI/ML","CS","IT","Data Science"],30)
}

df = pd.DataFrame(data)
df["Total"] = df["Maths"] + df["Science"] + df["English"] + df["Computer"]
df["Average"] = df["Total"] / 4
df["Grade"] = df["Average"].apply(lambda x:
    "A" if x>= 90 else "B" if x>=75 else "C" if x>=60 else "D")

print("Dataset created with shape:",df.shape)
print(df.head())

#Step 2:Basic Statistics
print("\n   DATASET STATISTICS   ")
print("Average marks:",round(df["Average"].mean(),2))
print("Highest average:",round(df["Average"].max(),2))
print("Lowest average:",round(df["Average"].min(),2))
print("\nGrade Distribution:\n",df["Grade"].value_counts())
print("\nCourse Distribution:\n",df["Course"].value_counts())

#Step 3:Visualization Dashboard
fig = plt.figure(figsize=(16,12))
fig.suptitle("Student Performance Analysis Dashboard",fontsize=18)

#Plot 1:Average marks bar chart
ax1 = fig.add_subplot(3,3,1)
top10 = df.nlargest(10,"Average")
sns.barplot(x="Average",y="Name",data=top10,palette="Blues_r",ax=ax1)
ax1.set_title("Top 10 students")
ax1.set_xlabel("Average marks")

#Plot 2:Grade Distribution pie chart
ax2 = fig.add_subplot(3,3,2)
grade_counts = df["Grade"].value_counts()
ax2.pie(grade_counts,labels=grade_counts.index,autopct="%1.1f%%",colors=["gold","lightblue","lightgreen","salmon"])
ax2.set_title("Grade Distribution")

#Plot 3:Course Distribution count plot
ax3 = fig.add_subplot(3,3,3)
sns.countplot(x="Course",data=df,palette="Set2",ax=ax3)
ax3.set_title("Students per course")
ax3.tick_params(axis="x",rotation=45)

#Plot 4:Marks Distribution Histogram
ax4 = fig.add_subplot(3,3,4)
sns.histplot(df["Average"],kde=True,color="purple",bins=10,ax=ax4)
ax4.set_title("Average Marks Distribution")
ax4.set_xlabel("Average marks")

#Plot 5:Subject comparison box plot
ax5 = fig.add_subplot(3,3,5)
subject_data =df[["Maths","Science","English","Computer"]]
subject_data.boxplot(ax=ax5)
ax5.set_title("Subject Marks Comparison")
ax5.set_ylabel("Marks")

#Plot 6:Correlation heatmap
ax6 = fig.add_subplot(3,3,6)
corr = df[["Maths","Science","English","Computer"]].corr()
sns.heatmap(corr,annot=True,fmt=".2f",cmap="coolwarm",ax=ax6,linewidths=0.5)
ax6.set_title("Subject Correlation")

#Plot 7:City Distribution
ax7 = fig.add_subplot(3,3,7)
sns.countplot(x="City",data=df,palette="Set3",ax=ax7)
ax7.set_title("Students per city")
ax7.tick_params(axis="x",rotation=45)

#Plot 8:Average marks by course
ax8 = fig.add_subplot(3,3,8)
sns.barplot(x="Course",y="Average",data=df,palette="muted",ax=ax8)
ax8.set_title("Average marks by course")
ax8.tick_params(axis="x",rotation=45)

#Plot 9:Scatter plot age vs average
ax9 = fig.add_subplot(3,3,9)
sns.scatterplot(x="Age",y="Average",data=df,hue="Grade",palette="Set1",s=100,ax=ax9)
ax9.set_title("Age vs Average Marks")
ax9.grid(True)

plt.tight_layout()
plt.savefig("day54_student_dashboard.png")
plt.show()
print("\nComplete dashboard saved as day54_student_dashboard.png")
 
#Step 4:Save final report
df.to_csv("Student_analysis_report.csv",index=False)
print("Report saved as student_analysis_report.csv")