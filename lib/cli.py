from models.genre import Genre
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
genres = Genre.get_all()


def main():
    print('\nwelcome to the Library Manager app!'
          '\nHere, you can manage all Books and Genres available in the store'
          '\nTo navigate the menu below, simply type the number of the desired option\n')
    main_menu()
    while True:
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            genres_menu()
        elif choice == "2":
            books_menu()
        else:
            print("\nInvalid choice")


def main_menu():
    print("\nYou´re currently on the main menu"
          "\nplease select one of the options below start navigating")
    print("\n1. Go to Genres menu")
    print("\n2. Go to Books menu")
    print("\n0. Exit the program")


def genres_menu():
    while True:
        print("You´re currently on the genre menu")
        print("\n1. See all genres")
        print("\n2. Add a new genre")
        print("\n3. Go back to the main menu")
        choice = input(">")
        if choice == "1":
            display_genre_menu()
        elif choice == "2":
            create_genre()
        elif choice == "3":
            main_menu()


def display_genre_menu():
    list_genres()
    print("Choose a genre to see more options:")
    user_choice = input(">")
    if user_choice == '0':
        genres_menu()
    else:
        list_genre_books(user_choice)

    


def books_menu():
    print("\n1. See all books")

if __name__ == "__main__":
    main()


"""     genre menu
            see all
            add one
    
    1
    2
    3
    4

        see all boooks
        update_genre
        delete_genre
        go back to genre menu """
