#Day 28 :Regex Basics

import re

#1.Basic pattern matching with search()
text = "My phone number is 9876543210"
match = re.search(r"\d{10}",text)
if match :
    print("Found phone number:",match.group())

#2.findall() - finds all matches
text2 = "Contact us at 9876543210 or 9123456780"
numbers = re.findall(r"\d{10}",text2)
print("\nAll phone numbers:",numbers)

#3.match()- checks only at the beginning of the string
result = re.match(r"Hello","Hello World")
if result:
    print("\nString starts with 'Hello'")

#4.Validating an email using regex
def is_valid_email(email):
    pattern = r"[a-zA-Z0-9._]+@[a-zA-Z0-9]+\.[a-z]{2,3}$"
    return bool(re.match(pattern,email))

print("\nEmail check:")
print("test@gmail.com -",is_valid_email("test@gmail.com"))
print("invalid-email -",is_valid_email("invalid-email"))

#5.sub() -replacing text using a pattern
sentence = "I love Java.Java is great."
new_sentence = re.sub(r"Java","Python",sentence)
print("\nafter replace:",new_sentence)

#6.split() - splitting text using a pattern
data = "apple,banana;cherry mango"
words = re.split(r"[,;]+",data)
print("\nSplit words:",words)

#Mini Project :Simple Form Validator
def validate_phone(phone):
    return bool(re.match(r"\d{10}$",phone))

def validate_email(email):
    pattern = r"[a-zA-Z0-9._]+@[a-zA-z0-9]+\.[a-z]{2,3}$"
    return bool(re.match(pattern,email))

def validate_name(name):
    return bool(re.match(r"[A-Za-z]+$",name))

print("\n      FORM VALIDATOR        ")
name = input("Enter your name:")
phone = input("Enter your phone number:")
email = input("Enter your email:")

if validate_name(name):
    print("Name is valid.")
else:
    print("Invalid name.Only letters and spaces allowed.")

if validate_phone(phone):
    print("Phone number is valid.")
else:
    print("Invalid phone number.Must be 10 digits.")

if validate_email(email):
    print("Email is valid.")
else:
    print("Invalid email format.")