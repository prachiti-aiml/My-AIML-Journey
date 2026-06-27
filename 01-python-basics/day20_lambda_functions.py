#Day 20 :Lambda Functions

#1. Basic lambda function
square = lambda x: x * x
print("Square of 5:",square(5))

#2.Lambda with multiple arguments
add = lambda a,b:a + b
print("Sum:",add(10,20))

#3.Lambda inside a normal function (returning a function)
def multiplier(n):
    return lambda x: x * n

double = multiplier(2)
triple = multiplier(3)
print("Double of 7:",double(7))
print("Triple of 7:",triple(7))

#4.Using lambda with map()
numbers = [1,2,3,4,5]
square_numbers = list(map(lambda x: x * x,numbers))
print("Squared numbers:",square_numbers)

#5.Using lambda with filter()
even_numbers = list(filter(lambda x: x % 2 == 0,numbers))
print("Even numbers:",even_numbers)

#6.Using lambda iwth sorted
students = [("Asha",85),("Sam",72),("Riya",91)]
sorted_by_marks = sorted(students,key=lambda s:s[1],reverse=True)
print("Sorted by marks:",sorted_by_marks)

#Mini Project: Marks Processor using lambda
marks = [45,78,92,33,67,88,55,21,99,60]

passed = list(filter(lambda m: m >= 40,marks))
failed = list(filter(lambda m: m < 40,marks))
scaled_marks = list(map(lambda m: m + 5,marks))
sorted_marks = sorted(marks,key=lambda m:m,reverse=True)

print("\n      MARKS PROCESSOR    ")
print("Originnal marks:",marks)
print("Passed:",passed)
print("Failed:",failed)
print("After 5 bonus marks:",scaled_marks)
print("Sorted (highest first):",sorted_marks)