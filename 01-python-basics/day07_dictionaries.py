# Day 7: Dictionaries

#1.Creating a Dictionary
student = {
    "name": "Prachiti",
    "course": "AIML Enginering",
    "year": 1
}

#2.Accessing value
print("Name:",student["name"])
print("Year:",student.get("year"))

#3.Adding and updating value
student["college"] = "VPCOE"
student["year"] = 2
print(student)

#4.Removing a Key
student.pop("course")
print(student)

#5.Looping through a Dictionary
for key,value in student.items():
    print(key,"-",value)

#6.Cecking if a key exists
if "name" in student:
    print("Name exists in dictionary")

#7.Nested Dictionary
students = {
    "s1":{"name":"Prachiti","marks":85},
    "s2":{"name":"Asha","marks":92}
}
for sid,info in students.items():
    print(sid,":",info["name"],"-",info["marks"],"marks")

#8.Dictionary Comprehension
squares = {x:x*x for x in range(1,6)}
print(squares)