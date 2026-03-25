#Day 04 - Loops (For and While)

print("=" * 40)
print("Day 4 LOOPS")
print("=" * 40)

# Part 1 - For Loop Basics 
print("\n For Loop")

for i in range(1,6):
    print(f"Number : {i}")

#Part 2 - Print Even Numbers
print("\n Even Numbers 1-20")

for i in range(1,21):
    if i % 2 == 0:
        print(i,end=" ")
print()

#Part 3 - MUltiplication Table 
print ("\n Table of 5")

for i in range(1,11):
    print(f"5 x {i} = {5 * i}")

#Part 4 - Loop through list
print("\n My Subjects")

subjects = ["Python","Maths","AI&ML","Data Science"]

for subject in subjects :
    print(f"Subject : {subject}")

#Part 5 - While Loop
print("\n While Loop")

count = 1
while count <= 5:
    print(f"Count :{count}")
    count +=1

#Part 6 - Sum of NUmbers
print("\n Sum of 1 to 10")

total = 0
for i in range(1,11):
    total += i
print(f"Sum of 1 to 10 ={total}")

#Part 7 - Star Pattern
print("\n Star PAttern")

for i in range(1,6):
    print("*" * i)

#Part 8 - Guess the number game
print("\n Guess the Nunber Game")

secret = 7
attempts = 0

while True:
    guess = int(input("Guess number(1-10):"))
    attempts += 1

    if guess == secret :
        print(f"CORRECT ! You got it in {attempts} attempts!")
        break
    elif guess < secret :
        print("Too LOW! Try again!")
    else:
        print("Too HIGH! Try again!")