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

## Routes
The application has the following routes:

/ (homepage) - displays a list of users and courses  
/login - displays a login form and allows users to log in  
/signup - displays a signup form and allows users to create an account  
/profile - displays the user's profile information and allows them to create a study group for a course they are taking  
<div style="display:flex;justify-content:center;">
  <img src="project_images/study_flowchart.jpeg" alt="Study Buddy Flowchart" title="Study Buddy Flowchart" height="400" style="max-width:100%;">
</div>  

## Dependencies
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

# Results  
This is our homepage:  
<div style="display:flex;justify-content:center;">
  <img src="project_images/homepage.png" alt="website homepage" title="Website Homepage" style="max-width:100%;">
</div>  
The buttons change colors when you hover over them. We decided to go with an incredibly simple interface so that there is no way for users to get confused on where to go. This straightforward design allows for users to get where they need to go immediately; when a user clicks on the "Login" or "Sign Up" button, they are immediately redirected to the respective pages.  
  
These are our login and signup pages:  
<div style="display:flex;justify-content:center;">
  <img src="project_images/login.png" alt="website login" title="Website Login" style="max-width:100%;">
  <img src="project_images/signup.png" alt="website signup" title="Website Signup" style="max-width:100%;">
</div>  
Once a user logs in or signs up, they are redirected to the profile page where they can enter their name, course preferences, and other such information that will help us match them with an ideal study buddy. If they are already logged in and authenticated, clicking on any of the buttons on the home page will take them directly to the profile page as well.  
  
This is the profile page:   
<div style="display:flex;justify-content:center;">
  <img src="project_images/profile.png" alt="website profile page" title="Website Profile Page" height="400" style="max-width:100%;">
</div>
explain how far we functionally got and got to test
  
# Project Evolution / Narrative    
Overall, the application provides a simple and user-friendly interface for creating and joining study groups for courses, and demonstrates the use of Flask's authentication system and SQLite database.  
  
## Expectations vs Reality  
photos of mockups, photo of homepage of actual site here; images didn't display, so for sake of time we kept the design basic  
<div style="margin: 0 auto;">
  <div style="display:flex;justify-content:center;">
    <img src="project_images/studymainpage.png" alt="mockup website homepage" title="Mockup Website Homepage" height="400" style="max-width:100%;">
  </div>  
  <div style="display:flex;justify-content:center;">
    <img src="project_images/studyloginpage.png" alt="mockup website login" title="Mockup Website Login" height="400" style="max-width:100%;">
  </div>  
  <div style="display:flex;justify-content:center;">
    <img src="project_images/expectationsvsreality.png" alt="expectations versus reality meme" title="Project Expectations vs Reality" height="500" style="max-width:100%;">
  </div>  
</div>
  
## Problems along the way  
Of course, what is a good journey without some obstacles. We ran into many, some of which are:  
- User Authentication - Once logged in, you can't logout, and sometimes it leads to an authentication error and doesn't allow you to access the profile. When we ran the code and clicked the login, sign up, or profile buttons on the profile, it took us to a page that says "Unauthorized
The server could not verify that you are authorized to access the URL requested. You either supplied the wrong credentials (e.g. a bad password), or your browser doesn't understand how to supply the credentials required." Our hypothesis is that it is returning this error to us because we already logged in once. That is why we created a logout option in the app.py (although it doesn't show for some reason), and a profile button to just directly access the profile if we are already logged in. But we can't access the profile even if we click directly on the button on the homepage that should access it.  
  
How do we fix this?  
>>The solution we found: use this method "current_user.is_authenticated:" instead of looking if the user is logged in; this method is better because it is more reliable when it comes to determining whether a user has been authenticated with the application's built-in authentication system. "current_user.is_authenticated" is a method from Flask-Login that checks whether the user has been authenticated and logged in to the application, while "if 'user_id' in session:" checks whether the "user_id" is present in the Flask session, but not necessarily whether they have logged in using the application's authentication system.  
  
- Search/Add Course Button Error - Unless the course code is already in the database, it gives you an error that says there is no method to add the course.  
  
How do we fix this?  
>>The solution to this was>> HAVE TO COME BACK TO THIS AFTER SOLVING. 
  
- Google API Authentication - We tried to integrate Google logins and sign ups because we thought it would be easiest to manage if people just signed in through their google accounts, but it ended up making the site not work, so we aborted the mission after many attempts and finding many different keys of various names to make it work. With more time though, we can see ourselves actually implementing it.  
  
## Limitations of Project  
no logout button, don't have server so it doesnt keep user information after reloading, need enough people to make a match
   
## Frontend Roadmap
- [x] Set up a shared GitHub repository and invite the other team member.
- [x] Install necessary tools and libraries for Flask web development.
- [x] Design a basic user interface for the application, including the sign-up, login, and profile creation pages. You can use pen and paper or a simple wireframing tool.
- [x] Start implementing the frontend of the application using Flask and a templating engine like Jinja2. Focus on creating the main pages (sign-up, login, profile creation) with simple HTML forms and basic styling using CSS.
  
## Backend Roadmap
- [x] Research and choose a simple database management system (e.g., SQLite) for the project.
- [x] Install the chosen database and necessary libraries for connecting to the database from the Flask application.
- [x] Design a basic database schema with tables for user information and courses.
- [x] Set up the database in the development environment.
- [x] Create simple functions or classes to interact with the database (e.g., adding users, searching for courses).
- [x] Integrate the database with the frontend, so that user registration, login, and profile creation work with the backend.

# Credits

The Study Group Finder web application was created by Matthew Syrigos and Lily Ichise as a project for Problem Solving and Software Design.
