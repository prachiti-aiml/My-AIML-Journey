# Day 02 - Variables & Data Types 

#Part1 - What is a Variable?
print("=" * 40)
print(" Day 02 - Variables & Data Types")
print("=" * 40)

#Part 2- Types of Variables
print("\n Types of Variables")

#1.String-Text
name = "Prachiti Rakesh Sakpal"
city ="Dombivli"

#2.Integer-Whole Number
age  = 18
year = 2026

#3.Float-Decimal Number
weight =38.8
cgpa   = 9.2

#4.Boolean-Truew or False
is_student =True
is_working =False

#Print all Variables
print(f"Name      :{name}")
print(f"City      :{city}")
print(f"Age       :{age}")
print(f"Year      :{year}")
print(f"Weight    :{weight}")
print(f"Cgpa      :{cgpa}")
print(f"Is student:{is_student}")
print(f"Is Working:{is_working}")

#Part 3- Types of each variable
print("\n Variables Types ")
print(f"Type of name  :{type(name)}")
print(f"Type of age  :{type(age)}")
print(f"Type of is_student:{type(is_student)}")

#Part 4- String Operations
print("\n String Operations")

first_name = "Prachiti"
last_name  = "Sakpal"

#Join Strings 
full_name = first_name + " " + last_name
print(f"Full Name : {full_name}")

#Length of Strings
print(f"Name Length : {len(full_name)}")

#Uppercase & Lowercase
print(f"Uppercase : {full_name.upper()}")
print(f"Lowercase : {full_name.lower()}")
      
#Part 5- Type Conversion
print("\n Type Conversion")

#String to Integer
num_str = "100"
num_int =int(num_str)
print(f"String to Int :{num_int + 50}")

#Integer to string 
age_str = str(age)
print(f"Int to String : " + age_str + "years old")

    