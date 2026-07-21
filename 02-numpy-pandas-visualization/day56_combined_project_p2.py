#Day 56: Combined Project - Cleaning and Analysis(Part 2)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Step 1:Load dataset from Day 55
try:
    df = pd.read_csv("eda_dataset.csv")
    print("Dataset loaded successfully")
except:
    print("eda_dataset.csv not found - creating fresh dataset")
    np.random.seed(42)
    n = 100
    data = {
        "Student ID": range(1,n + 1),
        "Name": ["Student" + str(i) for i in range(1,n+1)],
        "Age":np.random.randint(18,25,n),
        "Gender":np.random.choice(["Male","Female"],n),
        "City":np.random.choice(["Mumbai","Delhi","Pune","Chennai","Bangalore"],n),
        "Course":np .random.choice(["AI/ML","CS","IT","Data Science"],n),
        "Study_Hours":np.random.uniform(1,10,n).round(1),
        "Maths":np.random.randint(40,100,n),
        "Science":np.random.randint(40,100,n),
        "English":np.random.randint(40,100,n),
        "Computer":np.random.randint(49,100,n),
        "Attendance":np.random.randint(60,100,n),
        "Average":np.random.randint(40,100,n)
    }
    df = pd.DataFrame(data)

print("\nDatset Shape:",df.shape)
print("\nFirst 5 rows:\n",df.head())

#Step 2:Bivariate Analysis
print("\n    BIVARIATE ANALYSIS    ")
fig,axes = plt.subplots(2,3,figsize=(15,10))
fig.suptitle("Bivariate Analysis",fontsize=16)

#Study Hours vs Average Marks
sns.scatterplot(x="Study_Hours",y="Average",data=df,hue="Grade",ax=axes[0,0])
axes[0,0].set_title("Study Hours vs Average Marks")
axes[0,0].grid(True)

#Average Marks by Course
sns.boxplot(x="Course",y="Average",data=df,palette="Set2",ax=axes[0,1])
axes[0,1].set_title("Average Marks by Course")
axes[0,1].tick_params(axis="x",rotation=45)

#Average Marks By Gender
sns.boxplot(x="Gender",y="Average",data=df,palette="pastel",ax=axes[0,2])
axes[0,2].set_title("Average Marks by Gender")

#Attendance by Average
sns.scatterplot(x="Attendance",y="Average",data=df,hue="Result",palette="Set1",ax=axes[1,0])
axes[1,0].set_title("Attendance VS Average Marks")
axes[1,0].grid(True)

#Average Marks by City
sns.barplot(x="City",y="Average",data=df,palette="muted",ax=axes[1,1])
axes[1,1].set_title("Average Marks by City")
axes[1,1].tick_params(axis="x",rotation=45)

#Gender vs Grade count
sns.countplot(x="Grade",hue="Gender",data=df,palette="Set2",ax=axes[1,2])
axes[1,2].set_title("Grade Distribution by Gender")

plt.tight_layout()
plt.savefig("day56_bivariate.png")
plt.show()
print("Bivariate analysis saved")

#Step 3:Correlation Analysis
print("\n    CORRELATION ANALYSIS    ")
numeric_cols = ["Age","Study_Hours","Maths","Science","English","Computer","Attendance","Average"]
corr_matrix = df[numeric_cols].corr()

plt.figure(figsize=(10,8))
sns.heatmap(corr_matrix,annot=True,fmt=".2f",cmap="coolwarm",linewidths=0.5)
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig("day56_correlation.png")
plt.show()
print("Correlation heatmap saved")

#Step 4:Groupby Analysis
print("\n      GROUP ANALYSIS   ")
print("\nAverage marks by course:\n",
      df.groupby("Course")["Average"].mean().round(2))
print("\nAverage marks by city:\n",
      df.groupby("City")["Average"].mean().round(2))
print("\nPass rate by course:\n",
      df.groupby("Course")["Result"].apply(
          lambda x: (x == "Pass").sum() / len(x) * 100).round(2))

#Step 5:Key Insights
print("\n    KEY INSIGHTS    ")
print("1.Total Students:",len(df))
print("2.Pass rate:",round((df["Result"]=="Pass").sum() / len(df) * 100,2),"%")
print("3.Top performing course:",df.groupby("Course")["Average"].mean().idxmax())
print("4.Top performing city:",df.groupby("City")["Average"].mean().idxmax())
print("5.Correlation of study hours with average:",
      round(df["Study_Hours"].corr(df["Average"]),2))
print("6.Correlation of attendance with average:",
      round(df["Attendance"].corr(df["Average"]),2))

#Step 6:Save analysis results
df.to_csv("eda_analysis.csv",index=False)
print("\nAnalysis saved as eda_analysis.csv")