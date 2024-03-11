from helpers import (
    exit_program,
    list_genres,
    create_genre,
    update_genre,
    delete_genre,
    list_books,
    find_book_by_title,
    create_book,
    update_book,
    delete_book,
    list_genre_books
)


def main():
    print('welcome to the Library Manager app!'
          '\Here, you can manage all Books and Genres available in the store'
          '\nTo navigate the menu below, simply type the number of the desired option')
    main_menu()
    while True:
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            genres_menu()
        elif choice == "2":
            books_menu()
        elif choice == "3":
            books_menu()
        elif choice == "4":
            delete_genre()
        elif choice == "5":
            list_books()
        elif choice == "6":
            find_book_by_title()
        elif choice == "7":
            create_book()
        elif choice == "8":
            update_book()
        elif choice == "9":
            delete_book()
        elif choice == "10":
            list_genre_books()
        else:
            print("\nInvalid choice")


def main_menu():
    print("\n1. Go to Genres menu")
    print("\n2. Go to Books menu")
    print("\n0. Exit the program")

def genres_menu():
    print("\n1. See all genres")
    print("\n2. Add a new genre")
    print("\n3. Update a genre")
    print("\n4. Delete a genre")
    print("\n5. Go back to the main menu")

def books_menu():
    print("\n1. See all books")

if __name__ == "__main__":
    main()