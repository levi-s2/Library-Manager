# lib/helpers.py
from models.genre import Genre
from models.book import Book

def exit_program():
    print("\nThank you for using the Library Manager app, see you soon!")
    exit()

# We'll implement the genre functions in this lesson


def list_genres():
    genres = Genre.get_all()
    print('\nThese are all the genres available at the moment:')
    for genre in genres:
        print(f'\n{genre.name}')


def find_genre_by_name():
    name = input("\nEnter the genre's name: ")
    genre = Genre.find_by_name(name)
    print(genre) if genre else print(
        f'\ngenre {name} not found')


def create_genre():
    name = input("\nEnter the genre's name: ")
    try:
        genre = Genre.create(name)
        print(f'\nSuccess: {genre}')
    except Exception as exc:
        print("\nError creating genre: ", exc)


def update_genre():
    id_ = input("\nEnter the genre's id: ")
    if genre := Genre.find_by_id(id_):
        try:
            name = input("\nEnter the genre's new name: ")
            genre.name = name
            genre.update()
            print(f'\nSuccess: {genre}')
        except Exception as exc:
            print("\nError updating genre: ", exc)
    else:
        print(f'\ngenre {id_} not found')


def delete_genre():
    id_ = input("\nEnter the genre's id: ")
    if genre := Genre.find_by_id(id_):
        genre.delete()
        print(f'\ngenre {id_} deleted')
    else:
        print(f'\ngenre {id_} not found')


# You'll implement the book functions in the lab

def list_books():
    books = Book.get_all()
    for book in books:
        print(book)


def find_book_by_title():
    title = input("Enter the book's title: ")
    book = Book.find_by_title(title)
    print(f'\n{book}') if book else print(
        f'\nbook {title} not found')


def create_book():
    title = input("Enter the book's title: ")
    author = input("Enter the book's author: ")
    genre_name = input("Enter the book's genre name:")
    try:
        book = Book.create(title, author, genre_name)
        print(f'Success: {book}')
    except Exception as exc:
        print("Error creating book: ", exc)


def update_book():
    id_ = input("Enter the book's id: ")
    if book := Book.find_by_id(id_):
        try:
            title = input("Enter the books's new title: ")
            book.title = title
            author = input("Enter the book's new job title:")
            book.author = author
            genre_id = input("Enter the books's new genre id: ")
            book.genre_id = genre_id
            book.update()
            print(f'Success: {book}')
        except Exception as exc:
            print("Error updating book: ", exc)
    else:
        print(f'book {id_} not found')


def delete_book():
    id_ = input("Enter the book's id: ")
    if book := Book.find_by_id(id_):
        book.delete()
        print(f'book {id_} deleted')
    else:
        print(f'book {id_} not found')


def list_genre_books():
    name = input("Enter the genre's name: ")
    if genre := Genre.find_by_name(name):
        for book in genre.books():
            print(book)
    else:
        print(f'genre {name} not found')
