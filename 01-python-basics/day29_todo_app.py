#Day 29:Mini Project - To-Do List App

todos = []

def show_menu():
    print("\n      TO-DO LIST MENU       ")
    print("1.Add a task")
    print("2.View all tasks")
    print("3.Mark task as done")
    print("4.Delete a task")
    print("5.Exit")

def add_task():
    task = input("Enter task:")
    todos.append({"task":task,"done":False})
    print("Task added:",task)

def view_task():
    if len(todos) == 0:
        print("No tasks yet.")
    else:
        print("\nYour tasks:")
        for i in range(len(todos)):
            status ="Done" if todos[i]["done"] else "Pending"
            print(i + 1,".",todos[i]["task"],"-",status)

def mark_done():
    view_task()
    if len(todos) > 0:
        num = int(input("Enter task number to mark as done:"))
        if 1 <= num <= len(todos):
            todos[num - 1]["done"] = True
            print("Task marked as done!")
        else:
            print("Invalid task number.")

def delete_task():
    view_task()
    if len(todos) > 0:
        num = int(input("Enter task number to delete:"))
        if 1 <= num <= len(todos):
            removed = todos.pop(num - 1)
            print("Deleted task:",removed["task"])
        else:
            print("Invalid task number.")

def save_tasks():
    with open("todos.txt","w")as file:
        for todo in todos:
            status = "Done" if todo["done"] else "Pending"
            file.write(todo["task"] + "-" + status + "\n")
    print("Tasks saved to todos.txt")

while True:
    show_menu()
    choice = input("Enter your choice (1-5):")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_task()
    elif choice == "3":
        mark_done()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        save_tasks()
        print("Goodbye!")
        break
    else:
        print("Invalid choice.Please enter 1-5.")
        