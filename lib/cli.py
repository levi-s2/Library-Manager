from helpers import (
    exit_program,
    list_genres,
    find_genre_by_name,
    find_genre_by_id,
    create_genre,
    update_genre,
    delete_genre,
    list_books,
    find_book_by_title,
    find_book_by_id,
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
            find_genre_by_name()
        elif choice == "3":
            find_genre_by_id()
        elif choice == "4":
            create_genre()
        elif choice == "5":
            update_genre()
        elif choice == "6":
            delete_genre()
        elif choice == "7":
            list_books()
        elif choice == "8":
            find_book_by_title()
        elif choice == "9":
            find_book_by_id()
        elif choice == "10":
            create_book()
        elif choice == "11":
            update_book()
        elif choice == "12":
            delete_book()
        elif choice == "13":
            list_genre_books()
        else:
            print("\nInvalid choice")


def menu():
    print("\nPlease select an option:")
    print("\n0. Exit the program")
    print("\n1. List all genres")
    print("\n2. Find genre by name")
    print("\n3. Find genre by id")
    print("\n4: Create genre")
    print("\n5: Update genre")
    print("\n6: Delete genre")
    print("\n7. List all books")
    print("\n8. Find book by title")
    print("\n9. Find book by id")
    print("\n10: Create book")
    print("\n11: Update book")
    print("\n12: Delete book")
    print("\n13: List all books in a genre\n")


if __name__ == "__main__":
    main()