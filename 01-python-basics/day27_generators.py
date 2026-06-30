#Day 27:Generators

#1. Basic generator function using yield
def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1

for num in count_up_to(5):
    print(num,end=" ")
print()

#2.Generator vs normal function (memory efficient)
def square_numbers(nums):
    for n in nums:
        yield n * n

squares = square_numbers([1,2,3,4,5])
print("\nSquare using generator:")
for sq in squares:
    print(sq,end= "")
print()

#3.Using next() manually
def simple_gen():
    yield "first"
    yield "second"
    yield "third"

gen = simple_gen()
print("\nUsing next():")
print(next(gen))
print(next(gen))
print(next(gen))

#4.Infinite generator (controlled with a break)
def infinite_counter():
    num = 1
    while True:
        yield num
        num += 1

print("\nFirst 5 values from inifinte generator:")
counter = infinite_counter()
for i in range(5):
    print(next(counter),end=" ")
print()

#5.Generator expression (like list comprehension but lazy)
gen_exp = (x * x for x in range(1,6))
print("\nGenerator expression output:")
for val in gen_exp:
    print(val,end=" ")
print()

#Mini Project :Even Number Generator with limit
def even_number_generator(limit):
    num = 0
    while num <= limit:
        yield num
        num += 2

print("\n           EVEN NUMBER GENERATOR           ")
limit = int(input("Enter a limit:"))
print("Even numbers up to",limit,":")
for even in even_number_generator(limit):
    print(even,end=" ")
print()