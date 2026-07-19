#Day 56:Combined Project - Cleaning and Analysis (Part 2)
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Step 1:Load dataset from Day 55
try:
    df = pd.read_csv("eda_dataset.csv")
    print("Dataset loaded successfully")
except:
    print("Creating fresh dataset")
    np.random.seed(42)
    n = 100
    data= {
        "Student ID":range(1,n + 1),
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
        "Attendance":np.random.randint(60,100,n),
        "Average":np.random.randint(40,100,n),
        "Grade":np.random.choice(["A","B","C","D"],n),
        "Result":np.random.choice(["Pass","Fail"],n)
    }
    df = pd.DataFrame(data)

print("Shape:",df.shape)

#Step 2:Final Complete Dashboard
fig = plt.figure(figsize=(18,14))
fig.suptitle("Complete Student EDA Dashboard",fontsize=20)

#Plot 1:Top 10 students
ax1 = fig.add_subplot(3,4,1)
top10 = df.nlargest(10,"Average")
sns.barplot(x="Average",y="Name",data=top10,palette="Blues_r",ax=ax1)
ax1.set_title("Top 10 students")
ax1.set_xlabel("Average")

#Plot 2:Grade pie chart
ax2 = fig.add_subplot(3,4,2)
grade_counts = df["Grade"].value_counts()
ax2.pie(grade_counts,labels=grade_counts.index,autopct="%1.1f%%",colors=["gold","lightblue","lightgreen","salmon"])
ax2.set_title("Grade Distribution")

#Plot 3:Course bar chart
ax3 = fig.add_subplot(3,4,3)
sns.countplot(x="Course",data=df,palette="Set2",ax=ax3)
ax3.set_title("Students per Course")
ax3.tick_params(axis="x",rotation=45)

#Plot 4:Gender count
ax4 = fig.add_subplot(3,4,4)
sns.countplot(x="Gender",data=df,palette="pastel",ax=ax4)
ax4.set_title("Gender Distribution")

#PLot 5:Average marks Histogram
ax5= fig.add_subplot(3,4,5)
sns.histplot(df["Average"],kde=True,color="Purple",bins=15,ax=ax5)
ax5.set_title("Average Marks Distribution")

#Plot 6:Study Hours vs Marks Scatter
ax6 = fig.add_subplot(3,4,6)
sns.scatterplot(x="Study_Hours",y="Average",data=df,hue="Grade",palette="Set1",ax=ax6)
ax6.set_title("Study Hours vs Marks")
ax6.grid(True)

#Plot 7:Box Plot by Course
ax7 = fig.add_subplot(3,4,7)
sns.boxplot(x="Course",y="Average",data=df,palette="Set3",ax=ax7)
ax7.set_title("Marks by Course")
ax7.tick_params(axis="x",rotation=45)

#Plot 8:Attendance vs Marks
ax8 = fig.add_subplot(3,4,8)
sns.scatterplot(x="Attendance",y="Average",data=df,hue="Result",palette="Set1",ax=ax8)
ax8.set_title("Attendance vs Marks")
ax8.grid(True)

#Plot 9:Subject Comparison
ax9 = fig.add_subplot(3,4,9)
subjects = ["Maths","Science","English","Computer"]
subject_means = [df[s].mean() for s in subjects]
ax9.bar(subjects,subject_means,color=["blue","green","orange","red"])
ax9.set_title("Subject Average Marks")
ax9.set_ylabel("Average")

#Plot 10:City Distribution
ax10 = fig.add_subplot(3,4,10)
sns.countplot(x="City",data=df,palette="muted",ax=ax10)
ax10.set_title("Students per City")
ax10.tick_params(axis="x",rotation=45)

#Plot 11:Correlation heatmap
ax11 = fig.add_subplot(3,4,11)
numeric_cols = ["Study_Hours","Maths","Science","English","Computer","Average"]
corr = df[numeric_cols].corr()
sns.heatmap(corr,annot=True,fmt=".1f",cmap="coolwarm",ax=ax11,linewidths=0.5,annot_kws={"size":7})
ax11.set_title("Correlation Heatmap")

#Plot 12:Pass/Fail pie chart
ax12 = fig.add_subplot(3,4,12)
result_counts = df["Result"].value_counts()
ax12.pie(result_counts,labels=result_counts.index,autopct="%1.1f%%",colors=["lightgreen","salmon"])
ax12.set_title("Pass vs Fail")
plt.tight_layout()
plt.savefig("day57_complete_dashboard.png")
plt.show()
print("Complete dashboard saved as day57_complete_dashboard.png")

#Step 3:Final Insights Report
print("\n      FINAL EDA INSIGHTS REPORT     ")
print("Total students:",len(df))
print("Pass Rate:",round((df["Result"]=="Pass").sum()/len(df) * 100,2),"%")
print("Overall Average:",round(df["Average"].mean(),2))
print("\nBest Course:",df.groupby("Course")["Average"].mean().idxmax())
print("Best City:",df.groupby("City")["Average"].mean().idxmax())
print("\nSubject Averages:")
for s in subjects:
    print("",s,":",round(df[s].mean(),2))
print("\nTop student:",df.loc[df["Average"].idxmax(),"Name"],"with average:",df["Average"].max())

#Step 4:Save final Report
df.to_csv("final_eda_report.csv",index=False)
print("\nfinal report saved as final_eda_report.csv")