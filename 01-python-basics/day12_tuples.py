#Day 12:Tuples

#1.Creating a Tuple
fruits = ("apple","banana","cheery","mango")
print(fruits)

#2.Accessing Tuples Elements
print("First fruit:",fruits[0])
print("Last fruit:",fruits[3])

#3.Tuples are Immutable - this would cause an error if uncommented
#fruits[0] = "orange"

#4.Tuple Unpacking
coordinates = (10,20)
x,y = coordinates
print("x:",x,"y:",y)

#5.Looping through a Tuple
for fruit in fruits:
    print("Fruit:",fruit)

#6.Tuple methods - count and index
numbers = (1,2,3,2,4,2,5)
print("Count of 2:",numbers.count(2))
print("Index of 3:",numbers.index(3))

#7.Nested Tuples
student = ("Prachiti",(18,"VPCOE"))
print("Name:",student[0])
print("Age:",student[1][0])
print("College:",student[1][1])

#Mini Project: Contact Book using Tuples
contacts = [
    ("Asha","9876543210"),
    ("Riya","9123456780"),
    ("Sam","9988776655")
]

print("\n     Contact Book    ")
for name,number in contacts:
    print(name,":",number)

search_name = input("\nEnter a name to search:")
found = False
for name,number in contacts:
    if name.lower() == search_name.lower():
        print(name,"s number is",number)
        found = True
        break

if not found:
    print("Contact not found:")