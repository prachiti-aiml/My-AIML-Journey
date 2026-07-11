#Day 49:Matplotlib Histograms and Scatter Plots
import matplotlib.pyplot as plt
import numpy as np

#1.Basic Histogram
marks = [45,78,92,33,67,88,55,21,99,60,72,85,91,40,65,78,55,88,76,95]

plt.figure(figsize=(8,5))
plt.hist(marks,bins=5,color="skyblue",edgecolor="black")
plt.title("Student Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Number of students")
plt.savefig("plot7_histogram.png")
plt.show()
print("Histogram Saved")

#2.Histogram with more bins
plt.figure(figsize=(8,5))
plt.hist(marks,bins=10,color="orange",edgecolor="black")
plt.title("Marks Distribution (10 bins)")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.savefig("plot8_histogram2.png")
plt.show()

#3.Multiple Histograms
class_a = [45,78,92,33,67,88,55,21,99,60]
class_b = [55,65,75,85,95,50,70,80,90,60]

plt.figure(figsize=(8,5))
plt.hist(class_a,bins=5,alpha=0.5,color="blue",label="Class A",edgecolor="black")
plt.hist(class_b,bins=5,alpha=0.5,color="red",label="Class B",edgecolor="black")
plt.title("Class A vs Class B Marks")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.legend()
plt.savefig("plot9_multi_hist.png")
plt.show()
print("Multiple histogram saved")

#4.Basic scatter plot
study_hours = [1,2,3,4,5,6,7,8,9,10]
exam_marks = [35,45,55,60,70,75,80,85,90,95]

plt.figure(figsize=(8,5))
plt.scatter(study_hours,exam_marks,color="red",s=150,marker="*",edgecolors="black",alpha=0.7)
plt.title("Styled Scatter Plot")
plt.xlabel("Study Hours")
plt.ylabel("Exam marks")
plt.grid(True)
plt.savefig("plot11_styled_scatter.png")
plt.show()

#5.Styled scatter plot
plt.figure(figsize=(8,5))
plt.scatter(study_hours,exam_marks,color="red",s=150,marker="*",edgecolors="black",alpha=0.7)
plt.title("Styled Scatter Plot")
plt.xlabel("Study Hours")
plt.ylabel("Exam Marks")
plt.grid(True)
plt.savefig("plot11_styled_scatter.png")
plt.show()

#6.Scatter with color mapping
x = np.random.rand(50)
y = np.random.rand(50)
colors = np.random.rand(50)
sizes = np.random.rand(50) * 500

plt.figure(figsize=(8,5))
plt.scatter(x,y,c=colors,s=sizes,alpha=0.5,cmap="viridis")
plt.colorbar()
plt.title("Scatter with Color Mapping")
plt.savefig("plot12_colormap_scatter.png")
plt.show()
print("Color mapped scatter saved")

#Mini Project:Student Performance Visualizer
students = ["Asha","Riya","Sam","Tom","Neha","Raj","Priya","Prachiti","Jay","Tina"]
study_hours = [2,5,1,7,4,3,8,6,2,9]
marks = [45,75,35,88,65,55,92,80,40,95]
plt.figure(figsize=(10,6))
plt.scatter(study_hours,marks,color="purple",s=200,edgecolors="black",zorder=5)
for i in range(len(students)):
    plt.annotate(students[i],(study_hours[i],marks[i]),textcoords="offset points",xytext=(5,5),fontsize=8)

plt.title("Student Performance:Study Hours vs Marks")
plt.xlabel("Study Hours Per Day")
plt.ylabel("Exam Marks")
plt.grid(True)
plt.savefig("plot13_student_performance.png")
plt.show()
print("Student performance plot saved")