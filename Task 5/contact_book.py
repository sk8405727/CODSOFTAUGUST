class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def view_contacts(self):
        if not self.contacts:
            print("Contact book is empty.")
        else:
            print("Contact List:")
            for i, contact in enumerate(self.contacts, start=1):
                print(f"{i}. {contact.name} - {contact.phone}")

    def search_contact(self, search_term):
        matching_contacts = []
        for contact in self.contacts:
            if search_term.lower() in contact.name.lower() or search_term in contact.phone:
                matching_contacts.append(contact)
        
        if not matching_contacts:
            print("No matching contacts found.")
        else:
            print("Matching Contacts:")
            for i, contact in enumerate(matching_contacts, start=1):
                print(f"{i}. {contact.name} - {contact.phone}")

    def update_contact(self, contact_index, new_contact):
        if 0 <= contact_index < len(self.contacts):
            self.contacts[contact_index] = new_contact
            print("Contact updated successfully.")
        else:
            print("Invalid contact index. Contact not updated.")

    def delete_contact(self, contact_index):
        if 0 <= contact_index < len(self.contacts):
            deleted_contact = self.contacts.pop(contact_index)
            print(f"Contact '{deleted_contact.name}' deleted successfully.")
        else:
            print("Invalid contact index. Contact not deleted.")

def main():
    contact_book = ContactBook()

    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter contact name: ")
            phone = input("Enter contact phone: ")
            email = input("Enter contact email: ")
            address = input("Enter contact address: ")
            new_contact = Contact(name, phone, email, address)
            contact_book.add_contact(new_contact)
            print("Contact added successfully.")

        elif choice == "2":
            contact_book.view_contacts()

        elif choice == "3":
            search_term = input("Enter search term (name or phone): ")
            contact_book.search_contact(search_term)

        elif choice == "4":
            try:
                contact_index = int(input("Enter the index of the contact to update: "))
                name = input("Enter updated contact name: ")
                phone = input("Enter updated contact phone: ")
                email = input("Enter updated contact email: ")
                address = input("Enter updated contact address: ")
                new_contact = Contact(name, phone, email, address)
                contact_book.update_contact(contact_index - 1, new_contact)
            except ValueError:
                print("Invalid input. Please enter a valid index.")

        elif choice == "5":
            try:
                contact_index = int(input("Enter the index of the contact to delete: "))
                contact_book.delete_contact(contact_index - 1)
            except ValueError:
                print("Invalid input. Please enter a valid index.")

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()