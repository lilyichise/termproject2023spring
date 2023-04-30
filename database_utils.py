###my database_utls.py####
import sqlite3


class StudyGroupDatabase:
    def __init__(self, db_path):
        self.db_path = db_path
        self.connection = self.connect()

    def connect(self):
        """This function creates a connection to the database"""
        return sqlite3.connect(self.db_path)

    def close(self):
        """This function closes the connection to the database"""
        self.connection.close()

    def add_user(self, email, password):
        """This function adds a new user to the database"""
        cursor = self.connection.cursor()

        cursor.execute(
            "INSERT INTO users (email, password) VALUES (?, ?)", (email, password))

        self.connection.commit()

    def get_user(self, user_id):
        """This function retrieves a user from the database"""
        cursor = self.connection.cursor()

        cursor.execute("SELECT * FROM users WHERE user_id=?", (user_id,))
        user = cursor.fetchone()

        return user

    def check_user(self, email, password):
        # query the database for a user with the given email and password
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            query = "SELECT user_id FROM users WHERE email = ? AND password = ?"
            cursor.execute(query, (email, password))
            result = cursor.fetchone()

            if result:
                # return the user ID if a match is found
                return result[0]
            else:
                # return None if no match is found
                return None

    def get_users(self):
        """This function retrieves all users from the database"""
        cursor = self.connection.cursor()

        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()

        return users

    def search_courses(self, search_term):
        """This function searches for courses in the database"""
        cursor = self.connection.cursor()

        if search_term:
            cursor.execute("SELECT * FROM Courses WHERE course_name LIKE ? OR course_code LIKE ?",
                           (f"%{search_term}%", f"%{search_term}%"))
        else:
            cursor.execute("SELECT * FROM Courses")

        courses = cursor.fetchall()
        return courses

    def get_course_by_code(self, code):
        """This function retrieves a course from the database by its code"""
        cursor = self.connection.cursor()

        cursor.execute("SELECT * FROM Courses WHERE course_code=?", (code,))
        course = cursor.fetchone()

        return course

    def get_user_course_preferences(self, user_id):
        cursor = self.connection.cursor()

        cursor.execute(
            "SELECT * FROM user_courses WHERE user_id=?", (user_id,))
        user_preferences = cursor.fetchone()

        return user_preferences

    def get_all_user_course_preferences(self):
        cursor = self.connection.cursor()

        cursor.execute("SELECT * FROM user_courses")
        all_preferences = cursor.fetchall()

        return all_preferences

    def get_user_data(self, user_id):
        """This function retrieves a user's data from the database"""
        cursor = self.connection.cursor()

        cursor.execute("""
            SELECT user_id, email, password
            FROM users
            WHERE user_id=?
        """, (user_id,))
        user_data = cursor.fetchone


def creating_database():
    connection = sqlite3.connect('study_groups.db')
    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        email TEXT UNIQUE NOT NULL,
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

    connection.commit()
    cursor.close()
    connection.close()


def delete_users_table():
    connection = sqlite3.connect('study_groups.db')
    cursor = connection.cursor()

    cursor.execute("DROP TABLE IF EXISTS Users")
    connection.commit()

    cursor.close()
    connection.close()




if __name__ == "__main__":
    delete_users_table()

    creating_database()
