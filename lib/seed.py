#!/usr/bin/env python3

from models.__init__ import CONN, CURSOR
from models.genre import Genre
from models.book import Book

def seed_database():
    Book.drop_table()
    Genre.drop_table()
    Genre.create_table()
    Book.create_table()

    # Create seed data

seed_database()
print("Seeded database")