# Importing the necessary classes.
from book import BookManager
from user import UserManager
from check import CheckoutManager

# Main menu where user will input his choice
def main_menu():
    print("\n\n\n############################")
    print("  Library Management System")
    print("############################")
    print("1. Add Book")
    print("2. List Books")
    print("3. Add User")
    print("4. List Users")
    print("5. Search User")
    print("6. Checkin Book")
    print("7. Checkout Book")
    print("8. Exit")
    print("----------------------------")
    choice = input("Enter choice: ")
    print("----------------------------")

    return choice

def search_menu():
    print("############")
    print("Search By")
    print("############")
    print("1. Name")
    print("2. User ID")
    print("----------------------------")
    search_choice = input("Enter Choice: ")
    print("----------------------------")

def main():

    # Objects referring to their Classes
    book_manager = BookManager()
    user_manager = UserManager()
    checkout_manager = CheckoutManager()

    while True:
        # Calling the "main menu" function and storing the choice received from it.
        choice = main_menu()

        # Proceeding further according to the choice.

        # If choice is to "Add Book"
        if choice == '1':
            title = input("Enter title: ")
            author = input("Enter author: ")
            isbn = input("Enter ISBN: ")
            book_manager.add_book(title, author, isbn)
            print("Book added.")

        # If choice is to "Display added books"
        elif choice == '2':
            book_manager.list_books()

        # If choice is to "Add user"
        elif choice == '3':
            name = input("Enter user name: ")
            user_id = input("Enter user ID: ")
            user_manager.add_user(name, user_id)
            print("User added.")

        # If command is to list users.
        elif choice == "4":
            user_manager.list_users()

        # If command is to Search User
        elif choice == '5':
            search_choice = search_menu()

            if(search_choice == "1"):
                name = input("Enter user name to search: ")
                found_user = user_manager.search_user_by_name(name)
                
                if(found_user):
                    print("User Found: ", found_user)
                else:
                    print("User not found!")

            elif(search_choice == "2"):
                id = input("Enter user name to search: ")
                found_user = user_manager.search_user_by_id(id)
                
                if(found_user):
                    print("User Found: ", found_user)
                else:
                    print("User not found!")

            else:
                print("Invalid Choice")

        # if choice is to "Checkout"
        elif choice == '6':
            user_id = input("Enter user ID: ")
            isbn = input("Enter ISBN of the book to checkout: ")
            CheckoutManager.checkout_book(user_id, isbn)
            print("Book checked out.")

        # To exit the LMS
        elif choice == '7':
            print("Exiting.")
            break

        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()