#Day 50:Matplotlib Subplots and Customization
import matplotlib.pyplot as plt
import numpy as np

#1.Basic subplots
fig,axes = plt.subplots(1,2,figsize=(12,5))

#First subplot -line plot
x = [1,2,3,4,5]
y = [10,20,15,25,30]
axes[0].plot(x,y,color="blue",marker="o")
axes[0].set_title("Line plot")
axes[0].set_xlabel("X axis")
axes[0].set_ylabel("Y axis")
axes[0].grid(True)

#Second subplot - bar plot
subjects = ["Maths","Science","English"]
marks = [78,85,92]
axes[1].bar(subjects,marks,color="orange",edgecolor="black")
axes[1].set_title("Bar Plot")
axes[1].set_xlabel("Subjects")
axes[1].set_ylabel("Marks")

plt.tight_layout()
plt.savefig("plot14_subplots.png")
plt.show()
print("Subjects saved")

#2.2x2 grid of subplots
fig,axes = plt.subplots(2,2,figsize=(12,10))

#Plot 1 -Line
x = np.linspace(0, 10, 100)
axes[0,0].plot(x,np.sin(x),color="blue")
axes[0,0].set_title("Sine Wave")
axes[0,0].grid(True)

#Plot 2 -Bar
months = ["Jan","Feb","Mar","Apr","May"]
sales = [15000,1800,22000,19000,25000]
axes[0,1].bar(months,sales,color="green",edgecolor="black")
axes[0,1].set_title("Monthly Sales")

#Plot 3 - Scatter
study = [1,2,3,4,5,6,7,8]
marks = [35,45,55,60,70,75,85,90]
axes[1,0].scatter(study,marks,color="red",s=100)
axes[1,0].set_title("Study vs Marks")
axes[1,0].grid(True)

#Plot 4-Histogram
data = [45,78,92,33,67,88,55,21,99,60,72,85,91,40,65,78,55,88,76,95]
axes[1,1].hist(data,bins=5,color="purple",edgecolor="black")
axes[1,1].set_title("Marks Distribution")
plt.tight_layout()
plt.savefig("plot15_grid_subplots.png")
plt.show()
print("Grid subplots saved")

#3.Pie Chart
labels = ["AI/ML","CS","IT","Data Science"]
sizes = [35,25,20,20]
colors = ["gold","lightblue","lightgreen","salmon"]
explode = (0.1,0,0,0)

plt.figure(figsize=(8,6))
plt.pie(sizes,explode=explode,labels=labels,colors=colors,autopct="%1.1f%%",shadow=True,startangle=140)
plt.title("Course Distribution")
plt.savefig("plot16_pie.png")
plt.show()
print("Pie chart saved")

#4.Adding Annotations
x = [1,2,3,4,5]
y = [10,20,15,25,30]

plt.figure(figsize=(8,5))
plt.plot(x,y,color="blue",marker="o")
plt.annotate("Highest point",xy=(5,30),xytext=(4,28),arrowprops=dict(arrowstyle="-"))
plt.title("Plot with Annotation")
plt.grid(True)
plt.savefig("plot17_annotation.png")
plt.show()

#Mini Project: Complete Student Dashboard
fig,axes = plt.subplots(2,2,figsize=(14,10))
fig.suptitle("Student Performance Dashboard",fontsize=16)

#Plot 1 - Mark bar chart
students = ["Prachiti","Asha","Riya","Sam","Tom"]
marks = [78,85,92,60,75]
axes[0,0].bar(students,marks,color="skyblue",edgecolor="black")
axes[0,0].set_title("Student Marks")
axes[0,0].set_ylabel("Marks")
axes[0,0].set_ylim(0,100)

#Plot 2 -Pie chart of grades
grades = ["A","B","C"]
counts = [2,2,1]
axes[0,1].pie(counts,labels=grades,autopct="%1.1f%%",colors=["gold","lightblue","salmon"])
axes[0,1].set_title("Grade Distribution")

#Plot 3 -Line chart of marks trend
days = [1,2,3,4,5]
prachiti = [65,70,72,75,78]
asha = [75,78,80,83,85]
axes[1,0].plot(days,prachiti,label="Prachiti",marker="o")
axes[1,0].plot(days,asha,label="Asha",marker="s")
axes[1,0].set_title("Marks Trend")
axes[1,0].set_xlabel("Test Number")
axes[1,0].set_ylabel("Marks")
axes[1,0].legend()
axes[1,0].grid(True)

#Plot 4-Histogram
all_marks = [78,85,92,60,75,88,45,95,72,65]
axes[1,1].hist(all_marks,bins=5,color="green",edgecolor="black")
axes[1,1].set_title("Marks Distribution")
axes[1,1].set_xlabel("Marks")
axes[1,1].set_ylabel("Frequency")

plt.tight_layout()
plt.savefig("plot18_student_dashboard.png")
plt.show()
print("Student dashboard saved as plot18_student_dashboard.png")