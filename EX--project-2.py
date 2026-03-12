'''2.Contact Book 
Develop a contact book that can save, edit, and search contacts. 
Handle errors such as duplicate entries, empty fields, and wrong phone number 
format'''

contacts = {}

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")

    if name == "" or phone == "":
        print("Error: Fields cannot be empty")
        return

    if name in contacts:
        print("Error: Contact already exists")
        return

    if not phone.isdigit() or len(phone) != 10:
        print("Error: Phone number must be 10 digits")
        return

    contacts[name] = phone
    print("Contact saved successfully")


def edit_contact():
    name = input("Enter name to edit: ")

    if name not in contacts:
        print("Error: Contact not found")
        return

    new_phone = input("Enter new phone number: ")

    if not new_phone.isdigit() or len(new_phone) != 10:
        print("Error: Invalid phone number")
        return

    contacts[name] = new_phone
    print("Contact updated successfully")


def search_contact():
    name = input("Enter name to search: ")

    if name in contacts:
        print("Name:", name)
        print("Phone:", contacts[name])
    else:
        print("Contact not found")


while True:
    print("\n--- Contact Book ---")
    print("1. Add Contact")
    print("2. Edit Contact")
    print("3. Search Contact")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        edit_contact()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        print("Exiting program")
        break
    else:
        print("Invalid choice")
