#Day 48:Matplotlib Basics

import matplotlib.pyplot as plt
import numpy as np

#1.Basic line plot
x = [1,2,3,4,5]
y = [10,20,15,25,30]

plt.figure(figsize=(8,5))
plt.plot(x,y)
plt.title("Basic line plot")
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.savefig("plot1_line.png")
plt.show()
print("Line plot saved as plot1_line.png")

#2.Styled line plot
plt.figure(figsize=(8,5))
plt.plot(x,y,color="red",linewidth=2,linestyle="--",marker="o",markersize=8)
plt.title("Styled Line Plot")
plt.xlabel("Days")
plt.ylabel("Sales")
plt.grid(True)
plt.savefig("plot2_styled.png")
plt.show()
print("Styled line plot saved")

#3.Multiple lines on same plot
y1 = [10,20,15,25,30]
y2 = [5,15,10,20,25]

plt.figure(figsize=(8,5))
plt.plot(x,y1,color="blue",label="Product A",marker="o")
plt.plot(x,y2,color="green",label="Prodcut B",marker="s")
plt.title("Multiple Line Plot")
plt.xlabel("Days")
plt.ylabel("Sales")
plt.legend()
plt.grid(True)
plt.savefig("plot3_multiple.png")
plt.show()
print("Multiple line plot saved")

#4.Bar plot
subjects = ["Maths","Science","English","History","Computer"]
marks = [78,85,62,90,95]

plt.figure(figsize=(8,5))
plt.bar(subjects,marks,color="skyblue",edgecolor="black")
plt.title("Student Marks by Subject")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.ylim(0,100)
plt.savefig("plot4_bar.png")
plt.show()
print("Bar plot saved")

#5.Horizontal Bar Plot
plt.figure(figsize=(8,5))
plt.barh(subjects,marks,color="orange",edgecolor="black")
plt.title("Horizontal Bar Plot")
plt.xlabel("Marks")
plt.ylabel("Subjects")
plt.savefig("plot5_hbar.png")
plt.show()
print("Horizontal bar plot saved")

#Mini Project:Monthly Sales Dashboard
months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
sales = [15000,18000,22000,19000,25000,28000,30000,27000,24000,26000,32000,35000]

plt.figure(figsize=(12,6))
plt.plot(months,sales,color="blue",linewidth=2,marker="o",markersize=6,label="Monthly Sales")
plt.fill_between(months,sales,alpha=0.3,color="blue")
plt.title("Monthly Sales Dashboard 2024")
plt.xlabel("Month")
plt.ylabel("Sales(INR)")
plt.legend()
plt.grid(True)
plt.savefig("plot6_sales_dashboard.png")
plt.show()
print("Sales dashboard saved as plot6_sales_dashboard.png")