def display_menu():
    print("\n==============================")
    print("    CONTACT BOOK MANAGER      ")
    print("==============================")
    print("1. View Contacts")
    print("2. Add New Contact")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

def contact_book():
    contacts = {}

    while True:
        display_menu()
        choice = input("\nEnter your choice (1-5): ")

        if choice == '1':
            if not contacts:
                print("\nYour contact book is empty.")
            else:
                print("\n--- Contact List ---")
                for name, phone in contacts.items():
                    print(f"Name: {name} | Phone: {phone}")

        elif choice == '2':
            name = input("\nEnter contact name: ").strip()
            if name in contacts:
                print(f"\nContact '{name}' already exists!")
            else:
                phone = input("Enter phone number: ").strip()
                contacts[name] = phone
                print(f"\nContact '{name}' added successfully! ✅")

        elif choice == '3':
            name = input("\nEnter name to search: ").strip()
            if name in contacts:
                print(f"\nFound! Name: {name} | Phone: {contacts[name]}")
            else:
                print(f"\nContact '{name}' not found.")

        elif choice == '4':
            name = input("\nEnter name to delete: ").strip()
            if name in contacts:
                del contacts[name]
                print(f"\nContact '{name}' deleted successfully. 🗑️")
            else:
                print(f"\nContact '{name}' not found.")

        elif choice == '5':
            print("\nExiting Contact Book. Goodbye! 👋")
            break
        else:
            print("\nInvalid choice! Please enter a number between 1 and 5.")

if __name__ == "__main__":
    contact_book()