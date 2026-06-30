#Day 25: OOP - Encapsulation

#1.Public,protected,and private attributes
class Student:
    def __init__(self,name,age,marks):
        self.name = name
        self._age = age
        self.__marks = marks

    def show_details(self):
        print("Name:",self.name)
        print("Age:",self._age)
        print("Marks:",self.__marks)

student1 = Student("Prachiti",18,85)
student1.show_details()

#2.Getters and Setters
class BankAccount:
    def __init__(self,owner,balance):
        self.owner = owner
        self.__balance = balance

    def get_balance(self):
        return self.__balance
    
    def set_balance(self,amount):
        if amount < 0:
            print("Balance cannot be negative")
        else:
            self.__balance = amount

    def deposit(self,amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Deposit amount must be positive")

    def withdraw(self,amount):
        if amount > self.__balance:
            print("Insufficient balance")
        else:
            self.__balance -= amount

account1 = BankAccount("Asha",1000)
print("\nInitial balance:",account1.get_balance())

account1.deposit(500)
print("After deposit:",account1.get_balance())

account1.withdraw(2000)
account1.withdraw(300)
print("After withdraw:",account1.get_balance())

account1.set_balance(-50)
account1.set_balance(2000)
print("After set_balance:",account1.get_balance())

#Mini Project:ATM Simmulator using Encapsulation
class ATM:
    def __init__(self,pin,balance):
        self.__pin = pin
        self.__balance = balance

    def check_balance(self,entered_pin):
        if entered_pin == self.__pin:
            print("Your balance is:",self.__balance)
        else:
            print("Incorrect PIN")

    def deposit(self,entered_pin,amount):
        if entered_pin == self.__pin:
            self.__balance += amount
            print("Deposited",amount,"| New Balance:",self.__balance)
        else:
            print("Incorrect PIN")

    def withdraw(self,entered_pin,amount):
        if entered_pin != self.__pin:
            print("Incorrect PIN")
        elif amount > self.__balance:
            print("Insufficient balance")
        else:
            self.__balance -= amount
            print("Withdrew",amount, "| New balance:",self.__balance)

print("\n       ATM SIMULATOR        ")
my_atm = ATM(1234,5000)

entered = int(input("Enter your PIN:"))
my_atm.check_balance(entered)
my_atm.deposit(entered,1000)
my_atm.withdraw(entered,2000)
my_atm.withdraw(entered,10000)