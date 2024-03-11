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
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            list_genres()
        elif choice == "2":
            create_genre()
        elif choice == "3":
            update_genre()
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


def menu():
    print("\nTo navigate the Program, please enter the number of the desired option:")
    print("\n0. Exit the program")
    print("\n1. Get a list of all Genres")
    print("\n2: Create a new genre")
    print("\n3: Update an existing genre")
    print("\n4: Delete an existing genre")
    print("\n5. Get a list of all available books")
    print("\n6. Find a especific book by title")
    print("\n7: Order a new Book")
    print("\n8: Update a existing book")
    print("\n9: Delete a book")
    print("\n10: Get a list of all books belonging to a genre\n")


if __name__ == "__main__":
    main()