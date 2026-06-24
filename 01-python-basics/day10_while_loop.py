#Day 10:While Loops

#1.Basic while loop - Countdown
count = 10
while count > 0:
    print(count)
    count -= 1
print("Countdown Finished!")

#2.While loop with a condition based on user input
total = 0
while True:
    num = input("Enter a number to add (or 'stop' to finish):")
    if num == "stop":
        break
    total += int(num)
print("Total sum:",total)

#3.Guess the number game
import random

secret_number = random.randint(1,10)
guess = None

while guess != secret_number:
    guess = int(input("Guess a number between 1 and 10:"))
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess . secret_number:
        print("Too high! Try again.")
    else :
        print("Correct! You guessed it.")