#Day 41 :Pandas Filtering

import pandas as pd

#Creating sample DataFrame
data = {
    "Name": ["Prachiti","Asha","Riya","Sam","Tom","Neha","Raj","Priya"],
    "Age" : [18,19,20,18,21,19,22,20],
    "Marks":[78,85,92,60,75,88,45,95],
    "City":["Mumbai","Delhi","Pune","Chennai","Bangalore","Mumbai","Delhi","Pune"],
    "Course":["AI/ML","CS","IT","AI/ML","CS","IT","AI/ML","CS"]
}

df = pd.DataFrame(data)
print("DataFrame:\n",df)

#1.Single condition Filtering
print("\nStudents with marks > 80:\n",df[df["Marks"] > 80])
print("\nStudents from Mumbai:\n",df[df["City"] == "Mumbai"])
print("\nStudents aged 18:\n",df[df["Age"] == 18])

#2.Multiple conditions
print("\nMarks > 70 AND City is Mumbai:\n",
      df[(df["Marks"] > 70) & (df["City"] == "Mumbai")])

print("\nMarks > 90 OR City is Delhi:\n",
      df[(df["Marks"] > 90) | (df["City"] == "Delhi")])

#3.NOT Condition
print("\nStudent NOT from Mumbai:\n",df[df["City"] != "Mumbai"])

#4.isin()filtering
cities = ["Mumbai","Pune"]
print("\nStudents from Mumbai or Pune:\n",df[df["City"].isin(cities)])

#5.between() filtering
print("\nstudents with marks between 70 and 90:\n",
      df[df["Marks"].between(70,90)])

#6.str.contains() filtering
print("\nCourses containing 'ML':\n",
      df[df["Course"].str.contains("ML")])

#7.query()method
print("\nUsing query - marks > 80:\n",df.query("Marks > 80"))

#Mini Project: Student Filter System
print("\n      STUDENT FILTER SYSTEM      ")
print("1.Filter by city")
print("2.Filter by minimum marks")
print("3.Filter by course")

choice = input("Enter choice (1-3):")

if choice == "1":
    city = input("Enter city name:")
    result = df[df["City"] == city]
    if len(result) == 0:
        print("No students found from",city)
    else:
        print("\nStudents from",city,":\n",result)

elif choice == "2":
    min_marks = int(input("Enter minimum marks:"))
    result = df[df["Marks"] >= min_marks]
    if len(result) == 0:
        print("No students found with marks >=",min_marks)
    else:
        print("\nStudents with marks >=",min_marks,":\n",result)
    
elif choice == "3":
    course = input("Enter course name:")
    result = df[df["Course"] == Course]
    if len(result) == 0:
        print("No students found in",course)
    else:
        print("\nStudents in",course,":\n",result)

else:
    print("Invalid choice.")