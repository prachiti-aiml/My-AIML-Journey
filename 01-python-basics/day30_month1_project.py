#Day 30 :Month 1 Capstone - Contact Management System

contacts = []

def show_menu():
    print("\n         CONTACT MANAGEMENT SYSTEM     ")
    print("1.Add contact")
    print("2.View all contacts")
    print("3.Search contact")
    print("4.Update contact")
    print("5.Delete contact")
    print("6.Save contacts to file")
    print("7.Exit")

def add_contact():
    name = input("Enter name:")
    phone =input("Enter phone number:")
    email = input("Enter email:")
    contacts.append({"name":name,"phone":phone,"email":email})
    print("Contact added:",name)

def view_contacts():
    if len(contacts) == 0:
        print("No contacts found.")
    else:
        print("\n    ALL CONTACTS     ")
        for i in range(len(contacts)):
            c = contacts[i]
            print(i + 1,".Name:",c["Name"],"|Phone:",c["phone"],"|Email:",c["email"])

def search_contact():
    name = input("Enter name to search:")
    found = False
    for c in contacts:
        if c["name"].lower() == name.lower():
            print("\nContact found:")
            print("Name:",c["name"],"|Phone:",c["phone"],"|Email:",c["email"])
            found = True
            break
        if not found:
            print("Contact not found.")

def update_contact():
    view_contacts()
    if len(contacts)> 0:
        num = int(input("Enter contact number to update:"))
        if 1 <= num <= len(contacts):
            print("Leave blank to keep existing value.")
            name = input("New name (" + contacts[num-1]["name"]+ "):")
            phone = input("New phone (" + contacts[num - 1]["phone"]+ "):")
            email = input("Ner email (" + contacts[num - 1]["email"]+ "):")
            if name:
                contacts[num - 1]["name"] = name
            if phone:
                contacts[num - 1]["phone"] = phone
            if email:
                contacts[num - 1]["email"] = email
            print("Contact updated.")
        else:
            print("Invalid contact number.")

def delete_contact():
    view_contacts()
    if len(contacts) > 0:
        num = int(input("Enter contact number to delete:"))
        if 1 <= num <= len(contacts):
            removed = contacts.pop(num - 1)
            print("Delete contact:",removed["name"])
        else:
            print("Invalid contact number.")

def save_contacts():
    with open("contacts.txt","w")as file:
        for c in contacts:
            file.writw(c["name"] + "|" + c["phone"] + "|" + c["email"] + "\n")
    print("Contacts saved to contacts.txt")

while True:
    show_menu()
    choice = input("Enter your choice (1-7):")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        update_contact()
    elif choice == "5":
        delete_contact()
    elif choice == "6":
        save_contacts()
    elif choice == "7":
        print("Goodbye! Month 1 Complete!")
        break
    else:
        print("Invalid choice.Please enter 1-7.")