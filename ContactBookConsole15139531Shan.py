# ContactBook stores all contacts as dictionaries in a list
ContactBook = [
    {'fname': 'Shan', 'lname': 'Chand', 'num': '234555', 'mail': 'shangeeth909@gmail.com', 'address': 'N/A'}
]


# Function to display the menu options
def display_menu():
    menu = {
        '1': 'Store details',
        '2': 'Retrieve details',
        '3': 'Update contact',
        '4': 'Delete contact',
        '5': 'View all contacts',
        '6': 'Exit'
    }
    for k, v in menu.items():  #k &v are keys and values in menu dictionary
        print(f"{k}. {v}")


# Function to store a new contact
def store_details():
    while True:
        fnam = input('Enter first name: ')
        lnam = input('Enter last name: ')
        num = input('Enter contact number: ')
        address = input('Enter address: ')
        mail = input('Enter email address: ')
        ContactBook.append({'fname': fnam, 'lname': lnam, 'num': num, 'mail': mail, 'address': address})
        #above append function has been used to store the details in contact book repeatedly unless the user press t
        c = input('Press T to terminate or any key to continue: ')
        if c == 'T' or c == 't':  # Allows user to exit input loop
            break

# Function to print a contact's details
def print_contact(contact):
    for key, value in contact.items():
        print(f"{key.capitalize()}: {value}")


# Function to retrieve a contact by first name
def retrieve_details():
    n = input('Enter the first name of the contact: ')#get input from user to search first name
    found = False
    for contact in ContactBook: #loops through all the contacts in contact book
        if contact['fname'] == n:  # Checks for exact match of first name
            print_contact(contact) #print_contact function has been called when first name is matched
            found = True
            break
    if not found:
        print("Contact not found.")


# Function to update contact details
def update_contact():
    n = input('Enter the first name of the contact to update: ')
    found = False
    for contact in ContactBook:
        if contact['fname'] == n:
            print("What would you like to update?")
            x = input('(n) Number, (m) Mail, (a) Address: ')
            if x == 'n':
                contact['num'] = input('Enter new number: ')
            elif x == 'm':
                contact['mail'] = input('Enter new email: ')
            elif x == 'a':
                contact['address'] = input('Enter new address: ')
            else:
                print("Invalid option.")
            print("Updated Contact:")
            print_contact(contact)
            found = True
            break
    if not found:
        print("Contact not found.")


# Simplified function to delete a contact
def delete_contact():
    n = input('Enter the first name of the contact to delete: ')
    for contact in ContactBook:
        if contact['fname'] == n:
            ContactBook.remove(contact)
            print("Contact deleted.")
            return         #This will exit the function immediately after deleting
    print("Contact not found.")  # if no match is found, this will print


# Function to view all stored contacts
def view_all_contacts():
    if not ContactBook:
        print("No contacts available.")
    else:
        for contact in ContactBook:
            print_contact(contact)
            print('-' * 30)



# Main loop to display menu and take user input
while True:
    display_menu()
    choice = input('Enter your choice: ')

    if choice == '1':
        store_details()
    elif choice == '2':
        retrieve_details()
    elif choice == '3':
        update_contact()
    elif choice == '4':
        delete_contact()
    elif choice == '5':
        view_all_contacts()
    elif choice == '6':
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice, please try again.")