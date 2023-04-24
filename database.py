import sqlite3

def creating_database():
    """This function creates a database"""
    connection = sqlite3.connect('study_groups.db')
    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        schedule TEXT
    )
    """)
    username_to_insert = 'user1'
    cursor.execute ("SELECT * FROM users WHERE username=?", (username_to_insert,))
    existing_user = cursor.fetchone()
    
    if not existing_user:
        cursor.execute("INSERT INTO users (username, password, schedule) VALUES (?,?,?)", (username_to_insert, 'password1', 'schedue1'))
        connection.commit()

    cursor.close()
    connection.close()

#creating_database()

def main():
    creating_database()

if __name__ == '__main__':
    main()