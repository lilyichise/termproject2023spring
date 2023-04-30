# termproject2023spring

# Study Group Finder

Study Group Finder is a Python Flask web application that allows users to sign up and create study groups for courses they are taking. It uses Flask's built-in authentication system and SQLite database to store user information and study group data.

# Installation

To run the application, you will need to have Python 3 and Flask installed. You can install Flask using pip:

Copy code
pip install flask
You will also need to have SQLite installed on your machine. SQLite comes pre-installed on many systems, but if it is not installed on your system, you can download it from the official SQLite website.

Once you have installed the required dependencies, you can clone the repository from GitHub:

bash
Copy code
git clone https://github.com/<your-username>/study-group-finder.git
Usage

To start the application, navigate to the study-group-finder directory and run the following command:

arduino
Copy code
flask run
This will start the application on http://localhost:5000/.

# Routes
The application has the following routes:

/ (homepage) - displays a list of users and courses
/login - displays a login form and allows users to log in
/signup - displays a signup form and allows users to create an account
/profile - displays the user's profile information and allows them to create a study group for a course they are taking
Dependencies
Python 3
Flask
SQLite
# Database Design

The application uses an SQLite database to store user information and study group data. The database has the following tables:

Users
user_id (primary key)
name
email
phone_number
password (encrypted)
Courses
course_id (primary key)
course_name
course_code
User_Courses
user_course_id (primary key)
user_id (foreign key referencing Users table)
course_id (foreign key referencing Courses table)
preferred_days
preferred_times
group_size_preference
work_style
goal
  
 ## Roadmap

- [x] Add/Delete Notice
- [x] Add/Delete Student Majors
- [x] Add Polls questions
- [ ] User Authentication
- [ ] Interaction between Django and React
  
  
Credits

The Study Group Finder web application was created by Matthew Syrigos and Lily Ichiseas a project for Problem Solving and Software Design.
