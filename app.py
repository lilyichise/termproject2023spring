import os
from flask_login import LoginManager, UserMixin, login_user, logout_user, current_user, login_required
from flask import Flask, render_template, redirect, url_for, session, request, g
from database_utils import StudyGroupDatabase

app = Flask(__name__)
app.secret_key = "1234python"

# set path for database
DATABASE = 'study_groups.db'


def get_db():
    """
    function to get database
    """
    if 'db' not in g:
        g.db = StudyGroupDatabase(DATABASE)
    return g.db


@app.teardown_appcontext
def close_connection(exception):
    db = g.pop('db', None)
    if db is not None:
        db.close()


@app.route('/')
def homepage():
    db = get_db()
    return render_template('homepage.html')


# Route for the login page
@app.route("/login")
def login():
    # check if the user is already logged in
    if 'user_id' in session:
        return redirect(url_for('homepage'))

    # handle the login form submission
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # check if the user exists in the database
        db = get_db()
        user_id = db.check_user(email, password)

        if user_id:
            # set the user_id session variable and redirect to the homepage
            user = User(user_id)
            login_user(user)
            return redirect(url_for('homepage'))
        else:
            # if the user does not exist, display an error message
            error = "Invalid email or password. Please try again."
            return render_template('login.html', error=error)

    # display the login form
    return render_template('login.html')

# create the route for the signup page


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    # check if the user is already logged in
    if 'user_id' in session:
        return redirect(url_for('homepage'))

    # handle the signup form submission
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        # add the user to the database and set the user_id session variable
        db = get_db()
        user_id = db.add_user(name, email, password)
        user = User(user_id)
        login_user(user)

        # redirect to the homepage
        return redirect(url_for('homepage'))

    # display the signup form
    return render_template('signup.html')


@app.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    # get the user's information from the database
    db = get_db()
    # Handle the course code search and add functionality
    if request.method == 'POST' and 'search_course_code' in request.form:
        # Get the course code entered by the user
        course_code = request.form['search_course_code']

        # Check if the course code already exists in the database
        if db.get_course_by_code(course_code) is not None:
            # If the course code already exists, set it as the selected option
            selected_course = course_code
        else:
            # If the course code does not exist, add it to the database
            db.add_course(course_code)
            selected_course = course_code

        # Get the user's data
        user_data = db.get_user_data(session['user_id'])
        return render_template('profile.html', user_data=user_data, selected_course=selected_course)

    # Handle the form submission
    elif request.method == 'POST':
        name = request.form['name']
        course_code = request.form['course_code']
        meet_days = request.form['meet_days']
        meet_times = request.form['meet_times']
        group_size = request.form['group_size']
        work_style = request.form['work_style']
        goal = request.form['goal']

        # Insert the form data into the database
        db.insert_user_data(session['user_id'], name, course_code,
                            meet_days, meet_times, group_size, work_style, goal)

        # Redirect to the profile page
        return redirect(url_for('profile'))

    # If the request method is GET, display the profile page with the user's data
    else:
        user_data = db.get_user_data(session['user_id'])
        return render_template('profile.html', user_data=user_data)


if __name__ == '__main__':
    app.run(debug=True)
