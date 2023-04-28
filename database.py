"""
OUR DATABASE DESIGN
Tables:
1. Users
user_id (primary key)
name
email
phone_number
password (encrypted)

2. Courses
course_id (primary key)
course_name
course_code

3. User_Courses
user_course_id (primary key)
user_id (foreign key referencing Users table)
course_id (foreign key referencing Courses table)
preferred_days
preferred_times
group_size_preference
work_style
goal

"""

import sqlite3


def creating_database():
    """This function creates a database"""
    connection = sqlite3.connect('study_groups.db')
    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        phone_number TEXT,
        password TEXT NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS courses (
        course_id INTEGER PRIMARY KEY,
        course_name TEXT NOT NULL,
        course_code TEXT UNIQUE NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS user_courses (
        user_course_id INTEGER PRIMARY KEY,
        user_id INTEGER NOT NULL,
        course_id INTEGER NOT NULL,
        preferred_days TEXT NOT NULL,
        preferred_times TEXT NOT NULL,
        group_size_preference TEXT NOT NULL,
        work_style TEXT NOT NULL,
        goal TEXT NOT NULL,
        FOREIGN KEY(user_id) REFERENCES users(user_id),
        FOREIGN KEY(course_id) REFERENCES courses(course_id)
    )
    """)

    # Insert sample data into the users table
    username_to_insert = 'user1'
    cursor.execute("SELECT * FROM users WHERE username=?",
                   (username_to_insert,))
    existing_user = cursor.fetchone()

    if not existing_user:
        cursor.execute("INSERT INTO users (name, email, password) VALUES (?,?,?)",
                       (username_to_insert, 'user1@example.com', 'password1'))
        connection.commit()

    cursor.close()
    connection.close()


# creating_database()

def main():
    creating_database()


if __name__ == '__main__':
    main()
