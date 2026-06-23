#Day 9: Math Operations

num1 = float(input("Enter first number:"))
num2 = float(input("Enter second number:"))

def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    if b==0:
        return "Cannot Divide by zero"
    return a/b

print("Addition:",add(num1,num2))
print("Subtraction:",subtract(num1,num2))
print("Multiplication:",multiply(num1,num2))
print("Division:",divide(num1,num2))

#Mini Project:Shopping Bill Calculator
def calculate_bill(price,quantity,discount_percent,tax_percent):
    subtotal = multiply(price,quantity)
    discount_amount = multiply(subtotal,discount_percent/100)
    after_discount = subtract(subtotal,discount_amount)
    tax_amount = multiply(after_discount,tax_percent/100)
    total = add(after_discount,tax_amount)
    return total

print("\n   Shopping Bill Calculator   ")
price = float(input("Enter price per item:"))
quantity = float(input("Enter quantity:"))
discount = float(input("Enter discount percent:"))
tax = float(input("Enter tax percent:"))

final_amount = calculate_bill(price,quantity,discount,tax)
print("TOtal amount to pay:",round(final_amount,2))
