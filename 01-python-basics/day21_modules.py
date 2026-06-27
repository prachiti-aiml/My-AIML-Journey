#Day 21:Modules and Packages

#1.Using a built-in module
import math
print("Square rrot if 25:",math.sqrt(25))
print("Value of pi:",math.pi)
print("Factorial of 5:",math.factorial(5))

#2.Importing specific functions from module
from random import randint,choice
print("Random number between 1-10:",randint(1,10))
print("Random choice:",choice(["apple","banana","cheery"]))

#3.Importing a module with an alias
import datetime as dt
today = dt.date.today()
print("Today's date:",today)

#4.Creating your own module
#Save this part separately as a file named my_module.py in the same folder:
#def greet(name):
#    return "Hello,"+name + "!"
#def add(a,b)
#    return a + b
#Then import it like this (uncomment once my_module.py exists):
#import my_module
#print(my_module.greet("Prachiti"))
#print(my_module.add(5,3))

#5.Checking what's inside a module
import math
print("\nSome functions in math module:",dir(math)[:10])

#Mini Project :Random Quote Generator using modules
import random

quotes = [
    "Believe in yourself.",
    "Consistency beats motivation.",
    "Small steps everyday lead to big results.",
    "Practice makes progress,not perfection."
]

print("\n    DAILY QUOTE GENERATOR    ")
print(random.choice(quotes))
print("\nWant another quote? Type 'yes' to get one,anything else to stop.")
while True:
    choice_input = input("Your choice:").strip().lower()
    if choice_input == "yes":
        print(random.choice(quotes))
    else:
        print("See you tomorrow!")
        break