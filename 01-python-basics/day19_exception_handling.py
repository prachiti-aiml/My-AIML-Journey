#Day 19 : Exception Handling

#1.Basic try-except
try:
    num = int(input("Enter a number:"))
    result = 10 / num
    print("Result:",result)
except ZeroDivisionError:
    print("Error:Cannot Divide by zero.")
except ValueError:
    print("Error:That was not a valid number")

#2.try-except-else
try:
    x = int(input("Enter another number:"))
except ValueError:
    print("Invalid input.")
else:
    print("You entered:",x)

#3.try-except-finally
try:
    file = open("notes.txt","r")
    print(file.read())
except FileNotFoundError:
    print("File not found.")
finally:
    print("Finished attempting to read the file.")

#4.Catching multiple exception in one block
try:
    value = int(input("Enter a number to check:"))
    print(10/value)
except(ValueError,ZeroDivisionError) as e:
    print("something went wrong:",e)

#5.Raising your own exception
def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    return age

try:
    check_age(-5)
except ValueError as e:
    print("Caught custom error:",e)

#Mini Project : Safe Calculator
def safe_divide(a,b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"
    
def safe_calculator():
    try:
        num1 = float(input("\nEnter first number:"))
        num2 = float(input("Enter second number:"))
        operation = input("choose operation (+,-,*,/):") 

        if operation == "+":
            print("Result:",num1+num2)
        elif operation == "-":
            print("Result:",num1-num2)
        elif operation == "*":
            print("Result:",num1*num2)
        elif operation == "/":
            print("Result:",safe_divide(num1,num2))
        else:
            print("Invalid operation.")
    except ValueError:
        print("Please enter valid numbers only.")

safe_calculator()
        