# lib/models/book.py
from models.__init__ import CURSOR, CONN
from models.genre import Genre


class Book:

    # Dictionary of objects saved to the database.
    all = {}

    def __init__(self, title, author, genre_id, id=None):
        self.id = id
        self.title = title
        self.author = author
        self.genre_id = genre_id

    def __repr__(self):
        return (
            f"<book {self.id}: {self.title}, {self.author}, " +
            f"genre ID: {self.genre_id}>"
        )

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if isinstance(title, str) and len(title):
            self._title = title
        else:
            raise ValueError(
                "title must be a non-empty string"
            )

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, author):
        if isinstance(author, str) and len(author):
            self._author = author
        else:
            raise ValueError(
                "author must be a non-empty string"
            )

    @property
    def genre_id(self):
        return self._genre_id

    @genre_id.setter
    def genre_id(self, genre_id):
        if type(genre_id) is int and Genre.find_by_id(genre_id):
            self._genre_id = genre_id
        else:
            raise ValueError(
                "genre_id must reference a genre in the database")

    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of book instances """
        sql = """
            CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY,
            title TEXT,
            author TEXT,
            genre_id INTEGER,
            FOREIGN KEY (genre_id) REFERENCES genres(id))
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """ Drop the table that persists book instances """
        sql = """
            DROP TABLE IF EXISTS books;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """ Insert a new row with the title, job title, and genre id values of the current book object.
        Update object id attribute using the primary key value of new row.
        Save the object in local dictionary using table row's PK as dictionary key"""
        sql = """
                INSERT INTO books (title, author, genre_id)
                VALUES (?, ?, ?)
        """

        CURSOR.execute(sql, (self.title, self.author, self.genre_id))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def update(self):
        """Update the table row corresponding to the current book instance."""
        sql = """
            UPDATE books
            SET title = ?, author = ?, genre_id = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.title, self.author,
                             self.genre_id, self.id))
        CONN.commit()

    def delete(self):
        """Delete the table row corresponding to the current book instance,
        delete the dictionary entry, and reassign id attribute"""

        sql = """
            DELETE FROM books
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        # Delete the dictionary entry using id as the key
        del type(self).all[self.id]

        # Set the id to None
        self.id = None

    @classmethod
    def create(cls, title, author, genre_id):
        """ Initialize a new book instance and save the object to the database """
        book = cls(title, author, genre_id)
        book.save()
        return book

    @classmethod
    def instance_from_db(cls, row):
        """Return an book object having the attribute values from the table row."""

        # Check the dictionary for  existing instance using the row's primary key
        book = cls.all.get(row[0])
        if book:
            # ensure attributes match row values in case local instance was modified
            book.title = row[1]
            book.author = row[2]
            book.genre_id = row[3]
        else:
            # not in dictionary, create new instance and add to dictionary
            book = cls(row[1], row[2], row[3])
            book.id = row[0]
            cls.all[book.id] = book
        return book

    @classmethod
    def get_all(cls):
        """Return a list containing one book object per table row"""
        sql = """
            SELECT *
            FROM books
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        """Return book object corresponding to the table row matching the specified primary key"""
        sql = """
            SELECT *
            FROM books
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_title(cls, title):
        """Return book object corresponding to first table row matching specified title"""
        sql = """
            SELECT *
            FROM books
            WHERE title is ?
        """

        row = CURSOR.execute(sql, (title,)).fetchone()
        return cls.instance_from_db(row) if row else None