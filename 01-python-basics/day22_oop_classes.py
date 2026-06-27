#Day 22:OOP - Classes and Objects

#1.Defining a simple class
class Student:
    college = "VPCOE"

    def set_details(self,age,name):
        self.name = name
        self.age = age
    
    def show_details(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("College:",self.college)

#2.Creating objects (instances) of the class
student1 = Student()
student1.set_details("Prachiti",18)
student1.show_details()

print()
student2 = Student()
student2.set_details("Asha",19)
student2.show_details

#3.Accessing attributes directly
print("\nStudent 1 name:",student1.name)

#4.A class with a method that returns a value 
class Calculator:
    def add(self,a,b):
        return a + b
    
    def multiply(self,a,b): 
        return a * b
    
calc = Calculator()
print("\n Addition:",calc.add(10,5))
print("\n Multiplication:",calc.multiply(10,5))

#Mini Project : Simple Library Book Manager
class Book:
    def set_details(self,title,author,available=True):
        self.title = title
        self.author = author
        self.available = available

    def show_details(self):
        status = "Available" if self.available else "Issued"
        print("Title:",self.title,"|Author:",self.author,"|Status:",status)
              
    def issue_book(self):
        if self.available:
            self.available = False
            print(self.title,"has been issued.")
        else:
            print(self.title,"is already issued.")
        
    def return_book(self):
        self.available = True
        print(self.title,"has been returned.")

book1 = Book()
book1.set_details('Python Basics','John Doe')

book2 = Book()
book2.set_details("AI Fundamentals","Jane Smith")

print("\n     LIBRARY      ")
book1.show_details()
book2.show_details()

print()
book1.issue_book()
book1.show_details()

print()
book1.return_book()
book1.show_details()