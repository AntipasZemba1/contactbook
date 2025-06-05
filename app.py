# List to store all contacts
contacts = []

# Function to add a contact
def add_contact():
    name = input("Enter name: ") # This will ask user for contact name
    phone = input("Enter phone number: ") # This will create a disctionary for the contact
    contacts.append(contact) # Add the contact to the list
    print("Contact added!\n") # Confirm addition

# Function to view all contacts
def view_contacts
    if not contacts:
        print("No contacts found.\n") # Inform if list is empty
    else
        print("\n📋 All Contacts:")
        for contact in contacts:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}")  # Display each contact
        print()

# Function to search for a contact by name
def search_contact():
    name = input("Enter name to search: ")  # Get name to search
    found = False
    for contact in contacts:
        if contact["name"].lower() == name.lower():  # Case-insensitive match
            print(f"Found: {contact['name']} - {contact['phone']}\n")  # Show found contact
            found = True
            break
    if not found:
        print("Contact not found.\n")  # Inform if not found

# Function to delete a contact by name
def delete_contact():
    name = input("Enter name to delete: ")  # Get name to delete
    for contact in contacts:
        if contact["name"].lower() == name.lower():  # Case-insensitive match
            contacts.remove(contact)  # Remove contact from list
            print("Contact deleted.\n")
            return

# Function to display the menu
def show_menu():
    print("📱 Contact Book")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

# 🔁 Main Loop to keep the program running until user exits
while True:
    show_menu()  # Show the menu
    choice = input("Choose an option (1-5): ")  # Get user choice

    if choice == "1":
        add_contact()  # Add a contact
    elif choice == "2":
        view_contacts()  # View all contacts
    elif choice == "3":
        search_contact()  # Search for a contact
    elif choice == "4":
        delete_contact()  # Delete a contact
    elif choice == "5":
        print("Goodbye!")  # Exit message
        break  # Exit the loop
    else:
        print("Invalid choice. Please try again.\n")  # Handle invalid input