#function to add a new contact to the contact list
def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter contact phone number: ")
    email = input("Enter contact email: ")

    
    contact = {
        'name': name,
        'phone': phone,
        'email': email
    }
    
    contacts.append(contact)
    print(f"Contact {name} added successfully!")
    main_menu()
#fuction to view all contacts in the contact list  
def view_contacts():
    if not contacts:
        print("No contacts found.")
        return
    
    print("\nContact List:")
    idx=1
    for contact in contacts:
        print(f"{idx}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")  
        idx += 1  
    main_menu()    

#function to search for a contact in the contact list        
def search_contact():
    search_name = input("Enter the name of the contact to search: ")
    found=False
    for contact in contacts:
        if search_name.lower() == contact['name'].lower():
            print(f"Contact found: Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
            found=True
            break
    
    if not found:
        print(f"No contacts found with the name {search_name}.")
        return
    
    print("\nSearch Results:")
    main_menu()

#function to delete a contact from the contact list             
def delete_contact():
    delete_name = input("Enter the name of the contact to delete: ")
    for contact in contacts:
        if delete_name.lower() == contact['name'].lower():
            contacts.remove(contact)
            print(f"Contact {delete_name} deleted successfully!")
            return
    
    print(f"No contacts found with the name {delete_name}.") 
    main_menu()

#function to display the main menu and handle user choices              
def main_menu():
    try:
        while True:
            print("\nContact List Menu:")
            print("1. Add a new contact")
            print("2. View all contacts")
            print("3. Search for a contact")
            print("4. Delete a contact")
            print("0. Exit")
            choice = input("Enter your choice: ")
            
            if choice == '1':
                add_contact()
            elif choice == '2':
                view_contacts()
            elif choice == '3':
                search_contact()
            elif choice == '4':
                delete_contact()
            elif choice == '0':
                print("Exiting the Contact List. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a number.")
contacts = []            
main_menu()            