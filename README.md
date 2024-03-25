# Library Manager

### [Youtube]

## Overview

The Library manager app allows you to easily add, update and delete books and genres, belonging to your book library.

### Features

- Display books and genres
- Add or delete data
- Filter books by genre
- Manage all genre options in a single menu

## Technologies Used

- Python 3.8
- SQLite

## Getting Started

> **Note:** The `$` symbol indicates a command that should be run in your terminal. Do not include it when running commands.

### Prerequisites

- Python 3.8 or higher
- pipenv

### Installation

1. Clone the repository

2. Navigate to the project directory

3. Install dependencies using pipenv
    ```s
    $ pipenv install
    ```

4. Activate the virtual environment
    ```s
    $ pipenv shell
    ```

5.  If you want to test the app before using it, type the following command
    to populate the database with some mock data:
    ```s
    $ python lib/seed.py
    ```

6. Run the following command to run the CLI to start the App
    ```s
    $ python lib/cli.py
    ```

6. Start navigating the menu by simply typing the option`s number that you
desire. The app will always give you important feedback as to where you are
located in the app and how to change menus. Enjoy!

### Inside the App

1. when you enter the app, you will be prompted to either go to genre or book menu.

     ### Genre Menu
     1. You can see all genres
     2. you can add a new genre to the collection
     3. And also, delete a genre(Once deleted, all books associated will also be removed)
        But dont worry, this option will give the user a confirmation prompt
     4. Once a genre is choosen, you can see all books belonging to it;
        Update the genre name;
     5. All books can be managed from inside the genre that you are looking at
    
    
     ### Book Menu
     1. You can see all books

        



