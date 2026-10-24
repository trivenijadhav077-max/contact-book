contacts = {}

while True:
    print("\n1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")
    print("6. Count contacts")

    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter contact name: ")
        if name in contacts:
            print("Contact already exists.")
        else:
            phone = input("Enter contact phone number: ")
            contacts[name] = phone
            print(f"Contact {name} added successfully.")

    elif choice == '2':
        if contacts:
            for name, phone in contacts.items():
                print(f"Name: {name}, Phone: {phone}")
        else:
            print("No contacts found.")

    elif choice == '3':
        search_name = input("Enter contact name to search: ")
        if search_name in contacts:
            print(f"Name: {search_name}, Phone: {contacts[search_name]}")
        else:
            print(f"Contact {search_name} not found.")

    elif choice == '4':
        delete_name = input("Enter contact name to delete: ")
        if delete_name in contacts:
            del contacts[delete_name]
            print(f"Contact {delete_name} deleted successfully.")
        else:
            print(f"Contact {delete_name} not found.")

    elif choice == '5':
        print("Exiting the contact book.")
        break

    elif choice == '6':
        print(f"Total contacts: {len(contacts)}")

    else:
        print("Invalid choice. Please try again.")
