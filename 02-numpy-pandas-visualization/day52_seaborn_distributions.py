#Day 52:Seaborn Distribution Plots

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#Creating sample data
np.random.seed(42)
marks = np.random.normal(70,15,200)
marks = np.clip(marks,0,100)

data = {
    "Name":["Student" + str(i) for i in range(1,51)],
    "Marks": np.random.normal(70,15,50).clip(0,100),
    "Study_Hours":np.random.uniform(1,10,50),
    "Age":np.random.randint(18,25,50),
    "Course":np.random.choice(["AI/ML","CS","IT","Data Science"],50),
    "City":np.random.choice(["Mumbai","Delhi","Pune","Chennai"],50)
}

df = pd.DataFrame(data)

#1.histplot - histogram with distribution curve
plt.figure(figsize=(8,5))
sns.histplot(marks,kde=True,color="blue",bins=20)
plt.title("Marks Distribution with KDE")
plt.xlabel("Marks")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("sns_dist1_hist.png")
plt.show()
print("Histplot saved")

#2.kdeplot - smooth distribution curve
plt.figure(figsize=(8,5))
sns.kdeplot(marks,color="red",linewidth=2,fill=True,alpha=0.3)
plt.title("KDE Plot of Marks")
plt.xlabel("Marks")
plt.tight_layout()
plt.savefig("sns_dist2_kde.png")
plt.show()
print("KDE plot saved")

#3.Multiple KDE plots 
class_a = np.random.normal(65,10,100)
class_b = np.random.normal(75,12,100)

plt.figure(figsize=(8,5))
sns.kdeplot(class_a,label="Class A",fill=True,alpha=0.3)
sns.kdeplot(class_b,label="Class B",fill=True,alpha=0.3)
plt.title("Class A vs Class B Distribution")
plt.xlabel("Marks")
plt.legend()
plt.tight_layout()
plt.savefig("sns_dist3_multi_kde.png")
plt.show()
print("Multiple KDE saved")

#4.ecdfplot - cumulative distribution
plt.figure(figsize=(8,5))
sns.ecdfplot(marks,color="green")
plt.title("Cumulative distribution of Marks")
plt.xlabel("Marks")
plt.ylabel("Proportion")
plt.grid(True)
plt.tight_layout()
plt.savefig("sns_dist4_ecdf.png")
plt.show()
print("ECDF plot saved")

#5.rugplot - marks on x axis
plt.figure(figsize=(8,5))
sns.histplot(marks,kde=True,color="purple",bins=15)
sns.rugplot(marks,color="red",height=0.05)
plt.title("Histogram with Rug Plot")
plt.tight_layout()
plt.savefig("sns_dist5_rug.png")
plt.show()
print("Rug plot saved")

#6.Distribution by category
plt.figure(figsize=(8,5))
sns.histplot(data=df,x="Marks",hue="Course",kde=True,bins=15,alpha=0.5)
plt.title("Marks Distribution by Course")
plt.tight_layout()
plt.savefig("sns_dist6_category.png")
plt.show()
print("Category distribution saved")

#Mini Project:Exam Score Analyzer
print("\n     EXAM SCORE ANALYZER   ")
print("Mean marks:",round(df["Marks"].mean(),2))
print("Median marks:",round(df["Marks"].median(),2))
print("Std deviation:",round(df["Marks"].std(),2))

fig,axes = plt.subplots(1,3,figsize=(15,5))
fig.suptitle("Exam Score Analysis",fontsize=14)

sns.histplot(df["Marks"],kde=True,ax=axes[0],color="blue")
axes[0].set_title("Marks Distribution")

sns.kdeplot(df["Marks"],ax=axes[1],fill=True,color="green",alpha=0.4)
axes[1].set_title("KDE of Marks")

sns.boxplot(x="Course",y="Marks",data=df,ax=axes[2],palette="Set2")
axes[2].set_title("Marks by Course")
axes[2].tick_params(aixs="x",rotation=45)

plt.tight_layout()
plt.savefig("sns_exam_analyzer.png")
plt.show()
print("Exam analyzer dashboard saved")