# Practical task to create a contact book 

contacts = []

def add_contact():
    name = input("Enter the name: ").strip()
    last_name = input("Enter the last name: ").strip()
    user_name = input("Enter the username: ").strip()
    phone = input("Enter the phone number: ").strip()
    email = input("Enter the email address: ").strip()

    contact = {
    "name":  name, 
    "last_name": last_name,
    "user_name": user_name,
    "phone": phone, 
    "email": email
    }
    
    contacts.append(contact)
    print("\nContact added succesfully!")

def search_contact(name):
    for contact in contacts:

        if contact["name"].lower() == name.lower():
            return contact
        return None

def delete_contact(name):
    contact = search_contact(name)

    if contact:
        contacts.remove(contact)
        print("\nContact removed successfully!")
    else:
        print("\nContact not found!")

def view_all():
    if not contacts:
        print("\nNo contacts available.")
        return
    
    print("\n--------------- CONTACT LIST ---------------")
    print(f"{'Name':<10}{'Last Name':<10}{'User Name':<10}{'Phone':<10}{'Email':<10}")
    print("-" * 60)

    for contact in contacts:
        print(f"{contact['name']:<10}{contact['last_name']:<10}{contact['user_name']:<10}{contact['phone']:<10}{contact['email']:<10}")


#Main Menu
while True:
    print("\n--------------- CONTACT BOOK MANAGEMENT SYSTEM---------------")
    print("1. Add a Contact")
    print("2. Search for a contact")
    print("3. Remove a contact")
    print("4. View all contacts")
    print("5. Exit") 

    choice = input("Choose an option below: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        name = input("Enter the name to search: ").strip()
        contact = search_contact(name)

        if contact:
            print("\nContact has been found")
            print(f"Name : {contact['name']}")
            print(f"Last Name : {contact['last_name']}")
            print(f"User Name : {contact['user_name']}")
            print(f"Phone : {contact['phone']}")
            print(f"Email : {contact['email']}")

        else:
            print("\nContact not found")

    elif choice == "3":
        name = input("Enter name to remove: ").strip()
        delete_contact(name)

    elif choice == "4":              
        view_all()

    elif choice == "5":
            print("\nThank you for using the Contact Booking Management System.")
            break
    else: 
        print("\nInvalid choice. Please select a number between 1 and 5.") 