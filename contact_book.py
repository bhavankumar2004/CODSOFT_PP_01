# Simple Contact Book Application

def show_menu():
    print("\n--- Contact Book Menu ---")
    print("1. View Contact List")
    print("2. Add Contact")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

def view_contacts(contacts):
    if not contacts:
        print("\nNo contacts found.")
    else:
        print("\n--- Contact List ---")
        for i, contact in enumerate(contacts):
            print(f"{i + 1}. Name: {contact['name']}, Phone: {contact['phone']}")

def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contacts.append({'name': name, 'phone': phone, 'email': email, 'address': address})
    print(f"Contact '{name}' added!")

def search_contact(contacts):
    search_term = input("Enter name or phone number to search: ")
    found_contacts = [contact for contact in contacts if search_term in contact['name'] or search_term in contact['phone']]
    if found_contacts:
        for contact in found_contacts:
            print(f"\nName: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}")
    else:
        print("No contact found with that search term.")

def update_contact(contacts):
    search_term = input("Enter the name of the contact to update: ")
    for contact in contacts:
        if search_term == contact['name']:
            print(f"\nUpdating contact for {contact['name']}. Leave blank to keep current value.")
            new_name = input(f"Enter new name (current: {contact['name']}): ") or contact['name']
            new_phone = input(f"Enter new phone (current: {contact['phone']}): ") or contact['phone']
            new_email = input(f"Enter new email (current: {contact['email']}): ") or contact['email']
            new_address = input(f"Enter new address (current: {contact['address']}): ") or contact['address']
            contact.update({'name': new_name, 'phone': new_phone, 'email': new_email, 'address': new_address})
            print(f"Contact '{new_name}' updated!")
            return
    print("No contact found with that name.")

def delete_contact(contacts):
    search_term = input("Enter the name of the contact to delete: ")
    for i, contact in enumerate(contacts):
        if search_term == contact['name']:
            deleted_contact = contacts.pop(i)
            print(f"Contact '{deleted_contact['name']}' deleted!")
            return
    print("No contact found with that name.")

def main():
    contacts = []
    while True:
        show_menu()
        choice = input("Choose an option: ")
        if choice == '1':
            view_contacts(contacts)
        elif choice == '2':
            add_contact(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            update_contact(contacts)
        elif choice == '5':
            delete_contact(contacts)
        elif choice == '6':
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
