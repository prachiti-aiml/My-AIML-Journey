#Day 23: OOP CONSTRUCTORS

#1.Class with a constructor
class Student:
    def __init__(self,name,age,college):
       self.name = name
       self.age = age
       self.college = college
    
    def show_details(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("College:",self.college)

#2.Creating objects - values passed directly at a creation
student1 = Student("Prachiti", 18, "VPCOE")
student1.show_details()

print()

student2 = Student("Asha", 19, "VPCOE")
student2.show_details()

#3.Constructor with default values
class Book:
    def __init__(self,title,author,available=True):
        self.title = title
        self.author = author
        self.available = available

    def show_details(self):
        status = "Available" if self.available else "Issued"
        print("Title:",self.title,"|Author:",self.author,"|Status:",status)

book1 = Book("Python Basics","John Doe")
book1.show_details()

#4.Constructor doing extra setup work
class BankAccount:
    def __init__(self,owner,balance=0):
        self.owner = owner
        self.balance = balance
        print(owner + "'s account created with balance:",balance)
    
    def deposit(self,amount):
        self.balance += amount

    def show_balance(self):
        print(self.owner,"'s balance:",self.balance)

account1 = BankAccount("Prachiti",500)
account1.deposit(500)
account1.show_balance()

#Mini Project: Student Result Card using Constructor

class ResultCard:
    def __init__(self,name,marks1,marks2,marks3):
       self.name = name
       self.marks1 = marks1
       self.marks2 = marks2
       self.marks3 = marks3
       self.total = marks1 + marks2 + marks3
       self.average = self.total / 3
    
    def get_grade(self):
        if self.average >= 90:
            return "A"
        elif self.average >= 75:
            return "B"
        elif self.average >= 60:
            return "C"
        else:
            return "D"
        
    def show_result(self):
        print("\n       RESULT CARD      ")
        print("Name:",self.name)
        print("Subject 1:",self.marks1)
        print("Subject 2:",self.marks2)
        print("Subject 3:",self.marks3)
        print("otal:",self.total)
        print("Average:",self.average)
        print("Grade:",self.get_grade())

result1 = ResultCard("Prachiti",85,90,78)
result1.show_result()

result2 = ResultCard("Asha",60,55,70)
result2.show_result()