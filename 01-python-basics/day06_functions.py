#Day 6:Functions

#Basic Functions with no Parameters
def greet():
    print("Hello,Welcome to Day 6!")
greet()

#2.Functions with Parameters
def greet_user(name):
    print(f"Hello,{name}!")
greet_user("Prachiti")

#3.Function with return value
def add_numbers(a,b):
    return a+b
result = add_numbers(5,3)
print("sum:",result)

#4.Function with Default Parameter value
def greet_with_default(name="Guest"):
    print(f"Hi,{name}!")
greet_with_default
greet_with_default("Asha")

#5.Function with Multiple return values
def get_min_max(numbers):
    return min(numbers),max(numbers)
low,high = get_min_max([4,9,1,7,3])
print("Min:",low,"max:",high)

#6.Function calling another Function
def square(x):
    return x * x

def sum_of_squares(a,b):
    return square(a)+square(b)
print("Sum of squares:",sum_of_squares(2,3))