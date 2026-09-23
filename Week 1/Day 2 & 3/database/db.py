import sqlite3

def create_connection():
    #Create dabase connection
    conn = sqlite3.connect('todo.db')

    #Create cursor to be able to do functionality to database
    cur = conn.cursor()
    return conn, cur

def create_tables():
    conn,cur = create_connection()
    #To be to create relationships between tables
    cur.execute('PRAGMA foreign_keys = ON;')

    #Create users Database table
    cur.execute("""CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            surname TEXT NOT NULL

    )""")

    #Create todo database table
    cur.execute("""CREATE TABLE IF NOT EXISTS todos(
                todo_id INTEGER PRIMARY KEY,
                title TEXT NOT NULL,
                complete_status BOOLEAN NOT NULL DEFAULT 0 CHECK (complete_status IN (0,1)),
                user_id INTEGER NOT NULL,
                FOREIGN KEY (user_id) REFERENCES users (id)
    )""")
    conn.commit()
    conn.close()

def create_user(name,surname):
    conn,cur = create_connection()
    cur.execute('INSERT INTO users (name,surname) VALUES(?,?)', (name,surname))

    conn.commit()
    conn.close()
    return cur.lastrowid


create_tables()