#Day 26:Recursion Advanced

#1.Fibonacci sequence using recursion
def fibonacci(n):
    if n<= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print("Fibonacci sequence (first 10 terms):")
for i in range(10):
    print(fibonacci(i),end=" ")
print()

#2.Sum of a list using recursion
def recursive_sum(lst):
    if len(lst) == 0:
        return 0
    return lst[0] + recursive_sum(lst[1:])

numbers = [1,2,3,4,5]
print("\nSum of list:",recursive_sum(numbers))

#3.Reverse a string using recursion
def reverse_string(s):
    if len(s) == 0:
        return s
    return reverse_string(s[1:]) + s[0]

print("Reversed string:",reverse_string("python"))

#4.Power calculation using recursion
def power(base,exp):
    if exp == 0:
        return 1
    return base * power(base, exp - 1)

print("2 to the power 5:",power(2,5))

#5.Counting digits in a number using recursion 
def count_digits(n):
    if n == 0:
        return 0
    return 1 + count_digits(n // 10)

print("Digits in 123456:",count_digits(123456))

#Mini Project:Recursive Maze Step Counter (simplified)
def count_ways(n):
    if n <= 1:
        return 1
    return count_ways(n - 1) + count_ways(n - 2)

print("\n         STAIRCASE PROBLEM        ")
stairs = int(input("Enter number of stairs:"))
print("Number of ways to climb",stairs,"stairs:",count_ways(stairs))