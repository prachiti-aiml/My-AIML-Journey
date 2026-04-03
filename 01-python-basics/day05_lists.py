#Day 5 - Lists

print("=" * 40)
print("Day 05 - Lists")
print("=" * 40)

# Part 1 : What is a list?
#List = Collection of items in one variable
#Like a shopping bag that holds many items!

print("\n My First List")

fruits = ["Apple","Banana","Mango","Orange","Grapes"]
print(f"Fruits  :{fruits}")
print(f"Total   :{len(fruits)}")
print(f"First   :{fruits[0]}")
print(f"Last    :{fruits[-1]}")

#Part 2 :Access items
print("\n Accesss items")

marks = [85,92,78,95,88]
print(f"All Marks   :{marks}")
print(f"First Mark  :{marks[0]}")
print(f"Second Mark :{marks[1]}")
print(f"Last Mark   :{marks[-1]}")

#Part 3 - list Operations 
print("\n List Operations")

subjects = ["Python","Maths","AI"]

#Add item 
subjects.append("ML")
print(f"After append :{subjects}")

#Insert at position 
subjects.insert(1,"English")
print(f"After insert :{subjects}")

#Remove item
subjects.remove("English")
print(f"After remove :{subjects}")

#Sort List
numbers = [5,2,8,1,9,3]
numbers.sort()
print(f"Sorted  :{numbers}")

#Reverse list
numbers.reverse()
print(f"Reversed   :{numbers}")

#Part 4 : Loop through the list
print("\n Students Marks")

student_marks = [85,92,45,38,78,55,90]
total = 0
for mark in student_marks:
    total+= mark

average = total / len(student_marks)
highest = max(student_marks)
lowest  = min(student_marks)

print(f"Marks  :{student_marks}")
print(f"Total  :{total}")
print(f"Average :{average:.2f}")
print(f"Highest :{highest}")
print(f"lowest  :{lowest}")

#Part 5 : List with If Else
print("\n Pass or Fail")

all_marks = [85,45,92,38,78,55,90]

for mark in all_marks:
    if mark >= 50:
        print(f"Marks {mark}-Pass")
    else:
        print(f"Marks {mark}-Fail")

#Part 6: My subjects List
print("\n My Aiml Subjects")

aiml_subjects = [
    "Python Programming",
    "Machine Learning",
    "Deep Learning",
    "Data Science",
    "Neural Networks"
]
for i,subject in enumerate(aiml_subjects,1):
    print(f" {i}. {subject}")

#Part 7 :Mini Project
print("\n Student Report")

names = ["Prachiti","Aaryaa","Jiya","Samruddhi"]
scores= [92,78,85,90]

for i in range(len(names)):
    if scores[i] >= 90:
       grade = "A+"
    elif scores[i] >= 80:
       grade = "A"
    else:
       Grade = "B"
    print(f"{names[i]:10} - Score: {scores[i]} | Grade :{grade}")