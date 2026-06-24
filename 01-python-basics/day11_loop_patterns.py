#DAy 11 : Loop Patterns

#1. Simple sqaure pattern
print("Sqaure Pattern:")
for i in range(5):
    for j in range(5):
        print("*",end="")
    print()

#2.Right-angled Triangle
print("\nTriangle Pattern:")
for i in range(1,6):
    for j in range(i):
        print("*",end=" ")
    print()

#3.Inverted Triangle
print("\nInverted Triangle Pattern:")
for i in range(5 , 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()

#4.Pyramid Pattern
print("\nPyramid Pattern:")
rows = 5
for i in range(rows):
    print(" " * (rows - i - 1), end="")
    for j in range(2*i+1):
        print("*",end="")
    print()

#Mini Project:Pattern selector Menu
def print_sqaure(n):
    for i in range(n):
        print("*" * n)

def print_triangle(n):
    for i in range(1,n+1):
         print("* " * i)

def print_pyramid(n):
    for i in range(n):
         print(" " * (n - i -1)+ "*" * (i + 1))

print("\n    Pattern Selector    ")
print("1.Square")
print("2.Triangle")
print("3.Pyramid")
choice = int(input("Choose a pattern (1-3):"))
size = int(input("Enter size:"))

if choice == 1:
    print_square(size)
elif choice == 2:
     print_triangle(size)
elif choice == 3:
     print_pyramid(size)
else:
    print("Invalid choice")
