# CLI Todo App

A simple command-line todo list app I built to practice working with APIs in Python. It talks to a fake REST API (JSONPlaceholder) so you can view, create, update, and delete todos right from your terminal.

Heads up: JSONPlaceholder is a *fake* API it pretends to save your changes and gives you back a success response, but nothing is actually stored on their server. So if you refresh, your "new" todos will be gone. It's just there for practicing.

## What it does

- View all todos
- Look up a todo by its ID
- Find all todos for a specific user
- Add a new todo
- Update an existing todo's title
- Delete a todo

## Getting started

You'll need Python installed. Then:

1. Clone or download this project.
2. (Optional but recommended) Create a virtual environment so you don't mess with your global Python packages:

   Activate it:
   - Mac/Linux: `source venv/bin/activate`
   - Windows: `venv\Scripts\activate`
3. Install the dependencies:


## Running it

(swap `main.py` for whatever your entry-point file is actually called)

You'll get a menu like this:
1. View all TODO's
2. View todo by todo ID
3. Find todos by userID
4. Create todo
5. Update todo
6. Delete todo
7. Exit

Just type the number of what you want to do and follow the prompts.

## Running the tests

This project uses `pytest`. The tests fake out all the network calls, so they'll run fine even with no internet connection.


The `-v` just makes it print out each test name as it runs, which is nice when you're new to pytest and want to actually see what's happening.

## Project structure
.
├── src/
│ └── api_client/
│ └── client.py # talks to the API (get/post/put/delete)
├── main.py # the menu / CLI loop
├── test_client.py # pytest tests for client.py
├── requirements.txt
└── README.md


## Why I built this

Mostly to get comfortable with:
- Making HTTP requests in Python (`requests`)
- Basic error handling so the app doesn't just crash on bad input or a dead connection
- Writing my first pytest tests

Still very much a work in progress / learning project, so go easy on the code -_-