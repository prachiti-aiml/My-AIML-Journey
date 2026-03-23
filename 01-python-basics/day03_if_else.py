#Day 03 - If Else Conditions

print("=" * 40)
print("Day 03 - If Else Conditions")
print("=" * 40)

#Part 1 - What is If Else?
#If Condition is True  - Do this
#If Condition is False - Do that

#Part 2 - If Else
print("\n If Else")
age =18
if age >=18:
   print("You are an Adult")
else:
   print("You qare Minor")

#Part 3 -Grade Checker
print("\n Grade Character")

marks = 85
if marks >= 90 :
   grade ="A+"
elif marks >= 80 :
   grade ="A"   
elif marks >= 70 :
   grade ="B"
elif marks >= 60 :
   grade ="C"
elif marks >= 50 :
   grade ="D"
else:
   grade =" F - Fail" 

print(f"Marks :{marks}")
print(f"Grade :{grade}")

#Part 4-Number Checker
print("\n Number checker")

number = 7
if number > 0 :
   print(f"{number} is POSITIVE")
elif number < 0 :
   print(f"{number} is NEGATIVE")
else:
   print(f"{number} is zero")

if number % 2 == 0:
   print(f"{number} is EVEN")
else :
   print(f"{number} is ODD")

#pART 5 - largest Number
print("\n Largest Number")

a = 45
b = 70
c = 24

if a > b and a > c :
   print(f"Largest number is {a}")
elif b > a and b > c :
   print(f"Largest number is {b}")
else :
   print(f"Largest number is {c}")

#Part 6 - LOgin System
#print("\n Login system")

username ="prachiti"
password ="aiml2026"

input_user = input("Enter username:")
input_pass = input("Enter password:")

if input_user == username and input_pass == password:
   print("Login successful! Welcome Prachiti!")
   print("Now you are logged in!")
else:
   print("Wrong username or password!")
   print("Please try again!")