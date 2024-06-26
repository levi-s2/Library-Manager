from models.genre import Genre
from helpers import (
    exit_program,
    list_genres,
    create_genre,
    update_genre,
    delete_genre,
    list_books,
    create_book,
    update_book,
    delete_book,
    list_genre_books,
    find_genre_by_id
)
genres = Genre.get_all()


def main():
    print('\nwelcome to the Library Manager app!'
          '\nHere, you can manage all Books and Genres available in the store'
          '\nTo navigate the menu below, simply type the number of the desired option')
    main_menu()
    

def main_menu():
    print("\nYou´re currently on the main menu"
          "\nplease select one of the options below start navigating")
    print("\n0. Exit the program")
    print("1. Go to Genres menu")
    print("2. Go to Books menu")
    while True:
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            genres_menu()
        elif choice == "2":
            books_menu()
        else:
            print("\nInvalid choice, please select one of the options above")


def genres_menu():
    print("You´re currently on the genre menu")
    print("\n0. Go back to the main menu")
    print("1. See all genres")
    while True:
        choice = input(">")
        if choice == "1":
            display_genre_menu()
        elif choice == "0":
            main_menu()
        else:
            print("\nInvalid choice, please select one of the options above")


def display_genre_menu():
    list_genres()
    print("\nChoose the number of the genre to see its options, or:")
    print("Press 0 to go back to the Main menu")
    print('Press A to Add a genre to the collection')
    print("Press D to delete a genre\n")
    while True:
        genres = Genre.get_all()
        user_choice = input(">")
        if user_choice == '0':
            main_menu()
        elif user_choice == "d":
             delete_menu()
        elif user_choice == "a":
            create_genre()
            display_genre_menu()
        elif int(user_choice) in range(len(genres) + 1):
            genre = genres[int(user_choice) - 1] 
            genre_options(genre)
        else:
            print("\nInvalid choice, please select one of the options above")


def books_menu():
    print("\nwelcome to the Books Section!\n"
          "Here, you can see all the books available without having to filter them by genre")
    print('\n0. Go back to main menu.')
    print("1. See all Books.")
    while True:
        choice = input(">")
        if choice == "1":
            display_books_menu()
        elif choice == "0":
            main_menu()
        else:
            print("\nInvalid choice, please select one of the options above")


def display_books_menu():
    list_books()
    print('\nto manage a book, or filter by genre, please, refer to the genre menu\n')
    print('0. Go to Main menu')
    print('1. Go to genre menu')
    while True:
        choice = input('>')
        if choice == '0':
            main_menu()
        elif choice == '1':
            genres_menu()
        else:
            print("\nInvalid choice, please select one of the options above")


def delete_menu():
    print('Caution!\n'
          'When you delete a genre, all books associated will also be removed\n')
    print('0. Go back to main menu')
    while True:
        choice = input('type the number of the genre to be deleted: ')
        if choice == '0':
            display_genre_menu()
        else:
            delete_genre(choice)
            display_genre_menu()
        

def genre_options(genre):
    while True:
        print(f"\nYou`re currently viewing all the options for the {genre.name} genre\n")
        print("\n0. Go back to genres list")
        print("1. See all books of the genre")
        print("2. Update this genre")
        choice = input('>')
        if choice == "0":
            display_genre_menu()
        elif choice == "1":
            book_in_genre_menu(genre)
        elif choice == "2":
            update_genre(genre)
        else:
            print("\nInvalid choice, please select one of the options above")

def book_in_genre_menu(genre):
    books = genre.books()
    list_genre_books(genre)
    while True:
        print('\nTo update or delete a book, please, select it`s number or :')
        print("0. Go back to genres list")
        print('Press A to Add a book to this genre')
        choice = input('>')
        if choice == "0":
            display_genre_menu()
        elif choice == 'a':
            create_book(genre)
            book_in_genre_menu(genre)
        elif int(choice) in range(len(books) + 1):
            chosen_book = books[int(choice) - 1]
            books_options(chosen_book)
        else:
            print("\nInvalid choice, please select one of the options above")


def books_options(chosen_book):
    book = chosen_book
    genre = find_genre_by_id(book.genre_id)
    while True:
        print(f'You´re viewing the options for the {book.title} book\n')
        print(f'0. Go back to {genre.name} options')
        print('1. Delete book')
        print('2. Update book')
        choice = input('>')
        if choice == '0':
            book_in_genre_menu(genre)
        elif choice == '1':
            delete_book(book.id)
            book_in_genre_menu(genre)
        elif choice == '2':
            update_book(book.id)
            book_in_genre_menu(genre)

        
        



if __name__ == "__main__":
    main()