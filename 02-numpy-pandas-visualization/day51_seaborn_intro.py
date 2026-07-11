#Day 51:Seaborn Introduction
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#Creating sample DataFrame
data = {
    "Name":["Prachiti","Asha","Riya","Sam","Tom","Neha","Raj","Priya"],
    "Age":[18,19,20,18,21,19,22,20],
    "Marks":[78,85,92,60,75,88,45,95],
    "City":["Mumbai","Delhi","Pune","Chennai","Bangalore","Mumbai","Delhi","Pune"],
    "Course":["AI/ML","CS","IT","AI/ML","CS","IT","AI/ML","CS"]
}

df = pd.DataFrame(data)

#1.Basic bar plot with seaborn
plt.figure(figsize=(8,5))
sns.barplot(x="Name",y="Marks",data=df,palette="Blues")
plt.title("Student Marks - Seaborn Bar Plot")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("sns_plot1_bar.png")
plt.show()
print("seaborn bar plot saved")

#2.Count Plot
plt.figure(figsize=(8,5))
sns.countplot(x="City",data=df,palette="Set2")
plt.title("Students per city")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("sns_plot2_count.png")
plt.show()
print("Box plot saved")

#3.Box plot
plt.figure(figsize=(8,5))
sns.boxplot(x="Course",y="Marks",data=df,palette="Set3")
plt.title("Marks Distribution by Course")
plt.tight_layout()
plt.savefig("sns_plot3_box.png")
plt.show()
print("Box plot saved")

#4.Violin plot
plt.figure(figsize=(8,5))
sns.violinplot(x="Course",y="Marks",data=df,palette="muted")
plt.title("Violin Plot - Marks by Course")
plt.tight_layout()
plt.savefig("sns_plot4_violin.png")
plt.show()
print("Violin plot saved")

#5.Scatter plot with seaborn
plt.figure(figsize=(8,5))
sns.scatterplot(x="Age",y="Marks",data=df,hue="Course",size="Marks",sizes=(50,200))
plt.title("Age vs Marks by Course")
plt.tight_layout()
plt.savefig("sns_plot5_scatter.png")
plt.show()
print("Scatter plot saved")

#6.Line plot with seaborn
days = pd.DataFrame({
    "Day":[1,2,3,4,5,6,7],
    "Sales":[15000,18000,22000,19000,25000,28000,30000]
})
plt.figure(figsize=(8,5))
sns.lineplot(x="Day",y="Sales",data=days,marker="o",color="blue",linewidth=2)
plt.title("Daily Sales Trend")
plt.grid(True)
plt.tight_layout()
plt.savefig("sns_plot6_line.png")
plt.show()
print("Line plot saved")

#Mini Project:Student Analysis Dashboard with Seaborn
fig,axes = plt.subplots(2,2,figsize=(14,10))
fig.suptitle("Student Analysis Dashboard",fontsize=16)

sns.barplot(x="Name",y="Marks",data=df,palette="Blues",ax=axes[0,0])
axes[0,0].set_title("Marks by Student")
axes[0,0].tick_params(axis="x",rotation=45)

sns.boxplot(x="Course",y="Marks",data=df,palette="Set2",ax=axes[0,1])
axes[0,1].set_title("Marks Distribution by Course")

sns.countplot(x="City",data=df,palette="Set3",ax=axes[1,0])
axes[1,0].set_title("Student per city")
axes[1,0].tick_params(axis="x",rotation=45)

sns.scatterplot(x="Age",y="Marks",data=df,hue="Course",ax=axes[1,1])
axes[1,1].set_title("Age vs Marks")
plt.tight_layout()
plt.savefig("sns_student_dashboard.png")
plt.show()
print("Student dashboard saved")