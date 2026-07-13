#Day 53: Seaborn Heatmaps

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#Creating sample DataFrame
np.random.seed(42)
data = {
    "Maths": np.random.randint(50,100,10),
    "Science": np.random.randint(50,100,10),
    "English": np.random.randint(50,100,10),
    "History": np.random.randint(50,100,10),
    "Computer": np.random.randint(50,100,10)
}

df = pd.DataFrame(data)
print("DataFrame:\n",df)

#1.Basic correlation heatmap
plt.figure(figsize=(8,6))
correlation = df.corr()
sns.heatmap(correlation,annot=True,cmap="coolwarm",fmt=".2f",linewidth=0.5)
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig("sns_heat!_correlation.png")
plt.show()
print("Correlation heatmap saved")

#2.Heatmap with different colormap
plt.figure(figsize=(8,6))
sns.heatmap(correlation,annot=True,cmap="Blues",fmt=".2f",linewidths=0.5)
plt.title("Correlation Heatmap - Blues")
plt.tight_layout()
plt.savefig("sns_heat2_blues.png")
plt.show()

#3.Heatmap without annotations
plt.figure(figsize=(8,6))
sns.heatmap(correlation,cmap="YlOrRd",linewidths=0.5)
plt.title("Heatmap without Annotations")
plt.tight_layout()
plt.savefig("sns_heat3_no_annot.png")
plt.show()

#4.Masked heatmap (upper triangle)
mask = np.triu(np.ones_like(correlation,dtype=bool))
plt.figure(figsize=(8,6))
sns.heatmap(correlation,mask=mask,annot=True,cmap="coolwarm",fmt=".2f",linewidths=0.5)
plt.tight_layout()
plt.savefig("sns_heat4_masked.png")
plt.show()
print("Masked heatmap saved")

#5.Heatmap from pivot table
sales_data = {
    "Month":["Jan","Feb","Mar","Jan","Feb","Mar","Jan","Feb","Mar"],
    "Product":["Laptop","Laptop","Laptop","Phone","Phone","Phone","Tablet","Tablet","Tablet"],
    "Sales":[50000,45000,60000,30000,35000,28000,25000,22000,30000]
}

sales_df = pd.DataFrame(sales_data)
pivot = sales_df.pivot_table(values="Sales",index="Product",columns="Month")
plt.figure(figsize=(8,5))
sns.heatmap(pivot,annot=True,fmt=".0f",cmap="YlGn",linewidths=0.5)
plt.title("Sales Heatmap by Product and Month")
plt.tight_layout()
plt.savefig("sns_heat5_pivot.png")
plt.show()
print("Pivot heatmap saved")

#Mini Project:Student Performance Heatmap
students = ["Prachiti","Asha","Riya","Sam","Tom"]
subjects = ["Maths","Science","English","History","Computer"]
scores = np.array([
    [78,82,70,85,90],
    [85,79,90,75,88],
    [92,88,75,80,95],
    [60,55,60,65,70],
    [75,72,80,78,82]
])

score_df =pd.DataFrame(scores,index=students,columns=subjects)
plt.figure(figsize=(10,6))
sns.heatmap(score_df,annot=True,fmt="d",cmap="RdYlGn",linewidths=0.5,vmin=0,vmax=100)
plt.title("Student Performance Heatmap")
plt.savefig("sns_student_heatmap.png")
plt.show()
print("\n STUDENT PERFORMANCE HEATMAP   ")
print("Average marks per subject:\n",
      score_df.mean().round(2))
print("\nAverage marks per student:\n",
      score_df.mean(axis=1).round(2))
print("\nCorrelational Between subjects:\n",
      score_df.corr().round(2))