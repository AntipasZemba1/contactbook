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