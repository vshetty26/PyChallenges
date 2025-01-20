import os

file_name = "contacts.txt"

def add_contact(name, number, email):
    with open(file_name, "a") as file:
        file.write(f"{name},{number},{email}\n")

def search_contact(name):
    if not os.path.exists(file_name):
        return f"No contacts found."
    
    with open(file_name, "r") as file:
        for line in file:
            contact_name, contact_number, contact_email = line.strip().split(",")
            if contact_name.lower() == name.lower():
                return f"Name: {contact_name}, Number: {contact_number}, Email: {contact_email}"
    return "Contact not found."

def main():
    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Exit")
        
        choice = input("Enter your choice: ")
        if choice == "1":
            name = input("Enter name: ")
            number = input("Enter number: ")
            email = input("Enter email: ")
            add_contact(name, number, email)
            print("Contact added successfully!")
        elif choice == "2":
            name = input("Enter the name to search: ")
            result = search_contact(name)
            print(result)
        elif choice == "3":
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

main()
