#Day 13:Sets

#1.Creating a Sets
fruits = {"apple","banana","mango","cheery"}
print(fruits)

#2.Adding and Removing Elements
fruits.add("orange")
fruits.remove("banana")
print(fruits)

#3.Sets automatically remove duplicates
numbers = {1,2,2,3,3,4,5,5}
print(numbers)

#4.Sets Operation
set_a = {1,2,3,4,5}
set_b = {4,5,6,7,8}

print("Union:",set_a | set_b)
print("Intersection:",set_a & set_b)
print("Difference (A-B):",set_a - set_b)

#5.Checking Membership
print("Is 3 in set_a?",3 in set_a)

#6.Looping through a set
for item in fruits:
    print("Fruit:",item)

#Mini Project :Duplicate Remover and Common Friends Finder
my_list_with_duplicates = ["Asha","Riya","Sam","Tom"]
unique_names = set(my_list_with_duplicates)
print("\nUnique names:",unique_names)

my_friends = {"Asha","Riya","Sam","Tom"}
class_friends = {"Sam","Tom"}

common_friends = my_friends & class_friends
only_my_friends = my_friends - class_friends

print("\n   Friends Analysis   ")
print("Common friends:",common_friends)
print("Friends only in my list:",only_my_friends)