import sqlite3

def create_connection():
    #Create dabase connection
    conn = sqlite3.connect('todo.db')

    #Create cursor to be able to do functionality to database
    cur = conn.cursor()
    #To be to create relationships between tables
    cur.execute('PRAGMA foreign_keys = ON;')
    return conn, cur

def create_tables():
    conn,cur = create_connection()

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


def create_todo(title,user_id):
    conn,curr = create_connection()
    curr.execute('INSERT INTO todos (title,user_id) VALUES(?,?)', (title,user_id))

    conn.commit()
    conn.close()

    return curr.lastrowid

def get_user(userid):
    conn,curr = create_connection()
    curr.execute('SELECT * FROM users WHERE id = ?',(userid,))

    users = curr.fetchone()
    conn.close()
    return users

def get_todos():
    conn,curr = create_connection()
    curr.execute('SELECT * FROM todos')

    todo = curr.fetchall()
    conn.close()
    return todo

def get_todo_by_id(todo_id):
    conn,curr = create_connection()
    curr.execute('SELECT * FROM todos WHERE todo_id = ?', (todo_id,))

    todo = curr.fetchone()
    conn.close()
    return todo

def update_todo(todo_id,title,complete_status):
    conn,curr = create_connection()

    sql_prompt = """UPDATE todos
                    SET (title,complete_status) = (?,?)
                    WHERE todo_id = ?
    """
    curr.execute(sql_prompt,(title,complete_status,todo_id))
    conn.commit()
    conn.close()
    return True

def delete_todo(todo_id):
    conn,curr = create_connection()

    curr.execute('DELETE FROM todos WHERE todo_id = ?',(todo_id,))
    conn.commit()
    conn.close()
    return True

create_tables()