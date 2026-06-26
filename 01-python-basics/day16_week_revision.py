#Day 16:Week Revision - Mini Quiz Program"

score = 0
total_questions =5

print("     Python Mini Quiz    ")

print("Q1.What is the result of 8 *4 - 6?")
ans1 = int(input("Your answer:"))
if ans1 == (8 * 4 - 6):
    print("Correct!")
    score += 1
else:
    print("Wrong.Correct answer:",8 * 4 - 6)

print("\nQ2.How many times will this loop run?\ncount = 5\while count > 0:\n  count -= 1")
ans2 = int(input("Your answer:"))
if ans2 == 5:
    print("Correct!")
    score += 1
else:
    print("Worng. Correct answer:5")

print("\nQ3. How many stars are printed by:\nfor i in range(3):\n  print('*' * i)")
ans3 = int(input("Your answer:"))
if ans3 == 3:
    print("Correct! (0+1+2 = 3 stars total)")
    score+=1
else:
    print("Wrong. Correct answer:False")

print("\nQ5.What does [x*2 for x in range(3)] produce?")
print("a) [0,2,4] b)[1,2,3] c)[0,2,4]")
ans5 =input("Your answer (a/b/c):").strip().lower()
if ans5 == "a":
    print("Correct!")
    score += 1
else:
    print("Wrong. Correct answer:a) [0,2,4]")

print("\n      QUIZ RESULT        ")
print("You scored",score,"out of",total_questions)
if score == total_questions:
   print("Perfect score!")
elif score >= 3:
    print("Good job,keep practicing!")
else:
    print("Needs more revision on Day 9-15.")