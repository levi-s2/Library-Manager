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
    payroll = Genre.create("Payroll")
    human_resources = Genre.create("Human Resources")
    Book.create("Amir", "Accountant", payroll.id)
    Book.create("Bola", "Manager", payroll.id)
    Book.create("Charlie", "Manager", human_resources.id)
    Book.create("Dani", "Benefits Coordinator", human_resources.id)
    Book.create("Hao", "New Hires Coordinator", human_resources.id)


seed_database()
print("Seeded database")