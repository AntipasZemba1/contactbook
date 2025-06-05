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