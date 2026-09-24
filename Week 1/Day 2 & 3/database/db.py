import sqlite3

def create_connection():
    #Create dabase connection
    conn = sqlite3.connect('todo.db')

    #Create cursor to be able to do functionality to database
    cur = conn.cursor()
    #to create relationships between tables
    cur.execute('PRAGMA foreign_keys = ON;')
    return conn, cur

def create_tables():
    conn,cur = create_connection()

    try:
        cur.execute("""CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                surname TEXT NOT NULL,
                UNIQUE(name,surname)

        )""")

        cur.execute("""CREATE TABLE IF NOT EXISTS todos(
                    todo_id INTEGER PRIMARY KEY,
                    title TEXT NOT NULL,
                    complete_status BOOLEAN NOT NULL DEFAULT 0 CHECK (complete_status IN (0,1)),
                    user_id INTEGER NOT NULL,
                    FOREIGN KEY (user_id) REFERENCES users (id),
                    UNIQUE(title,user_id)
        )""")
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error creating tables: {e}")
        conn.rollback()
    finally:
        conn.close()

def create_user(name,surname):
    conn,cur = create_connection()

    try:
        cur.execute('INSERT INTO users (name,surname) VALUES(?,?)', (name,surname))
        conn.commit()
        return cur.lastrowid
    except sqlite3.IntegrityError as e:
        if "UNIQUE" in str(e):
            print(f"Error: user '{name} {surname}' already exists.")
        else:
            print(f"Error creating user: {e}")
        conn.rollback()
        return None
    except sqlite3.Error as e:
        print(f"Error creating user: {e}")
        conn.rollback()
        return None
    finally:
        conn.close()


def create_todo(title,user_id):
    conn,curr = create_connection()

    try:
        curr.execute('INSERT INTO todos (title,user_id) VALUES(?,?)', (title,user_id))
        conn.commit()
        return curr.lastrowid
    except sqlite3.IntegrityError as e:
        if "UNIQUE" in str(e):
            print(f"Error: user {user_id} already has a todo titled '{title}'.")
        elif "FOREIGN KEY" in str(e):
            print(f"Error: no user with id {user_id} exists.")
        else:
            print(f"Error creating todo: {e}")
        conn.rollback()
        return None
    except sqlite3.Error as e:
        print(f"Error creating todo: {e}")
        conn.rollback()
        return None
    finally:
        conn.close()

def get_user_todo(userid):
    conn,curr = create_connection()

    try:
        curr.execute('SELECT * FROM todos WHERE user_id = ?',(userid,))
        todo = curr.fetchall()
        return todo
    except sqlite3.Error as e:
        print(f"Error fetching todo for user {userid}: {e}")
        return None
    finally:
        conn.close()

def get_user_by_id(user_id):
    conn,curr = create_connection()
 
    try:
        curr.execute('SELECT * FROM users WHERE id = ?', (user_id,))
        user = curr.fetchone()
        return user
    except sqlite3.Error as e:
        print(f"Error fetching user {user_id}: {e}")
        return None
    finally:
        conn.close()


def get_todos():
    conn,curr = create_connection()

    try:
        curr.execute('SELECT * FROM todos')
        todo = curr.fetchall()
        return todo
    except sqlite3.Error as e:
        print(f"Error fetching todos: {e}")
        return []
    finally:
        conn.close()

def get_todo_by_id(todo_id):
    conn,curr = create_connection()

    try:
        curr.execute('SELECT * FROM todos WHERE todo_id = ?', (todo_id,))
        todo = curr.fetchone()
        return todo
    except sqlite3.Error as e:
        print(f"Error fetching todo {todo_id}: {e}")
        return None
    finally:
        conn.close()

def update_todo(todo_id,title,complete_status):
    conn,curr = create_connection()

    try:
        sql_prompt = """UPDATE todos
                        SET title = ?, complete_status = ?
                        WHERE todo_id = ?
        """
        curr.execute(sql_prompt,(title,complete_status,todo_id))
        conn.commit()

        if curr.rowcount == 0:
            print(f"No todo found with id {todo_id}.")
            return False
        return True
    except sqlite3.IntegrityError as e:
        if "UNIQUE" in str(e):
            print(f"Error: todo {todo_id} can't be renamed to '{title}', that title already exists for this user.")
        else:
            print(f"Error updating todo {todo_id}: {e}")
        conn.rollback()
        return False
    except sqlite3.Error as e:
        print(f"Error updating todo {todo_id}: {e}")
        conn.rollback()
        return False
    finally:
        conn.close()

def delete_todo(todo_id):
    conn,curr = create_connection()

    try:
        curr.execute('DELETE FROM todos WHERE todo_id = ?',(todo_id,))
        conn.commit()

        if curr.rowcount == 0:
            print(f"No todo found with id {todo_id}.")
            return False
        return True
    except sqlite3.Error as e:
        print(f"Error deleting todo {todo_id}: {e}")
        conn.rollback()
        return False
    finally:
        conn.close()

create_tables()