import sqlite3

class StudyGroupDatabase:
    def __init__(self, db_path):
        self.db_path = db_path

    def connect(self):
        """This function creates a connection to the database"""
        return sqlite3.connect(self.db_path)

    def add_user(self, name, email, password):
        """This function adds a new user to the database"""
        connection = self.connect()
        cursor = connection.cursor()

        cursor.execute("INSERT INTO users (name, email, password) VALUES (?, ?, ?)", (name, email, password))

        connection.commit()
        connection.close()

    def get_user(self, user_id):
        """This function retrieves a user from the database"""
        connection = self.connect()
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM users WHERE user_id=?", (user_id,))
        user = cursor.fetchone()

        connection.close()

        return user

    def search_courses(self, search_term):
        """This function searches for courses in the database"""
        connection = self.connect()
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM courses WHERE course_name LIKE ? OR course_code LIKE ?", (f"%{search_term}%", f"%{search_term}%"))
        courses = cursor.fetchall()

        connection.close()

        return courses
