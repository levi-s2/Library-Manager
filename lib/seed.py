#!/usr/bin/env python3

from models.__init__ import CONN, CURSOR
from models.genre import Genre
from models.book import Book

def seed_database():
    Book.drop_table()
    Genre.drop_table()
    Genre.create_table()
    Book.create_table()

    Fantasy = Genre.create('Fantasy')
    Romance = Genre.create('Romance')
    Poetry = Genre.create('Poetry')
    Tragedy = Genre.create('Tragedy')
    Epic = Genre.create('Epic')
    Fiction = Genre.create('Fiction')
    Modern = Genre.create('Modern ')
    Non_Fiction = Genre.create('Non Fiction')
    Terror = Genre.create('Terror')
    Biography = Genre.create('Biography')
    Novel = Genre.create('Novel')

    Book.create('fairy tale', 'Stephen King', Romance.id)
    Book.create('Don Quixote', 'Miguel de Cervantes', Fantasy.id)
    Book.create('The Divine Comedy', 'Dante Alighieri', Poetry.id)
    Book.create('The Great Gatsby', 'F. Scott Fitzgerald', Tragedy.id)
    Book.create('The Odyssey', 'Homer', Epic.id)
    Book.create('Moby Dick', 'Herman Melville', Epic.id)
    Book.create('War and Peace', 'Leo Tolstoy', Fiction.id)
    Book.create('In Search of Lost Time', 'Marcel Proust', Modern.id)
    Book.create('The Prince', 'Niccolo Machiavelli', Non_Fiction.id)
    Book.create('King Lear', 'William Shakespeare', Tragedy.id)
    Book.create('Alice`s Adventures in Wonderland', 'Lewis Carroll', Romance.id)
    Book.create('The old man and the sea', 'Earnest Hemmingway', Romance.id)
    Book.create('Harry Potter Collection', 'Jk Rowling', Fantasy.id)
    Book.create('It(Novel)', 'Stephen King', Terror.id)
    Book.create('Percy Jackson Collection', 'Rick Riordan', Fantasy.id)
    Book.create('A droga da obediência', 'Pedro Bandeira', Novel.id)
    Book.create('Game of Thrones', 'George R.R. Martin', Fantasy.id)
    Book.create('Cidades Mortas', 'Monteiro Lobato', Modern.id)
    Book.create('Antigone', 'Sophocles', Non_Fiction.id)
    Book.create('Cinema Speculation', 'Quentin Tarantino', Biography.id)
    Book.create('The Diary of Anne Frank', 'Anne Frank', Biography.id)

seed_database()
print('database seeded sucessfully')
