#Day 24:OOP - INHERITANCE

#1.Parent Class
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def show_details(self):
        print("Name:",self.name)
        print("Age:",self.age)

#2.Child class inheriting from person
class Student(Person):
    def __init__(self,name,age,college):
        super().__init__(name,age)
        self.college = college

    def show_details(self):
        super().show_details()
        print("College:",self.college)

student1 = Student("Prachiti", 18, "VPCOE")
student1.show_details()

3.#Another child class
class Employee(Person):
    def __init__(self,name,age,salary):
        super().__init__(name,age)
        self.salary = salary

    def show_details(self):
        super().show_details()
        print("Salary:",self.salary)

employee1 = Employee("Asha",25,35000)
print()
employee1.show_details()

#4.Method overriding
class Animal:
    def speak(self):
        print("This animal makes a sound")

class Dog(Animal):
    def speak(self):
        print("The dog barks")

class Cat(Animal):
    def speak(self):
        print("The cat meows")

print()
animals = [Dog(),Cat(),Animal()]
for animal in animals:
    animal.speak()

#Mini Project: School Management System using Inheritance
class SchoolMember:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def introduce(self):
        print("Name:",self.name,"|Age:",self.age)

class Teacher(SchoolMember):
     def __init__(self,name,age,subject):
            super().__init__(name,age)
            self.subject = subject
        
     def introduce(self):
        super().introduce()
        print("Role:Teacher | Subject:",self.subject)

class StudentMember(SchoolMember):
    def __init__(self,name,age,grade):
        super().__init__(name,age)
        self.grade = grade
        
    def introduce(self):
        super().introduce()
        print("Role:Student | Grade:",self.grade)

print("\n      SCHOOL MEMBERS     ")
teacher1 = Teacher("Mr.Sharma",40,"Mathematics")
teacher1.introduce()

print()
student2 = StudentMember("Riya",17,"12th")
student2.introduce()