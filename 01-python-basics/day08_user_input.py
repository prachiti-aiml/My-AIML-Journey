#Day 8:User Input

#Part 1: Basic user input
name = input("Enter your name:")
age  = input("Enter your age:")
print("Hello,",name,"! You are",age,"years old.")

age =int(age)
next_year_age = age+1
print("Next year you will be",next_year_age)

college = input("Enter your college name:")
goal = input("Enter your goal:")
print(name,"studies at",college,"and aims to",goal)

#Mini Project
def get_profile():
    profile={}
    profile["name"] = name
    profile["age"] = age
    profile["college"] = college
    profile["goal"] = goal
    return profile

def show_profile(profile):
    print("\n    Profile Card  ")
    print("Name :",profile["name"])
    print("Age :",profile["age"])
    print("College:",profile["college"])
    print("Goal :",profile["goal"])
    print("Next year age :",profile["age"]+1)

user_profile = get_profile()
show_profile(user_profile)    