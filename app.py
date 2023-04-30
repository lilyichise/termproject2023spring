####### Our App###################
# testing testing
import os
from flask_login import LoginManager, UserMixin, login_user, logout_user, current_user, login_required
from flask import Flask, render_template, redirect, url_for, session, request, g
from database_utils import StudyGroupDatabase
import sqlite3
from notification_utils import notify_match

app = Flask(__name__)
app.secret_key = "1234python"

# Puting a login manager to correct an error
login_manager = LoginManager()
login_manager.init_app(app)


class User(UserMixin):
    def __init__(self, user_id):
        self.id = user_id


@login_manager.user_loader
def load_user(user_id):
    """Load a user from the database using the user ID."""
    db = get_db()
    user_data = db.get_user(int(user_id))
    if user_data:
        return User(user_id)
    return None

#Didn't end up using the following commented form.
######## FOR DEPLOYMENT ###########
# db_url = os.environ.get('DATABASE_URL')

# if db_url:
#     # Use the environment variable to configure the database connection
#     app.config['DATABASE'] = db_url
# else:
#     # Use a default database path if the environment variable is not set
#     app.config['DATABASE'] = 'study_groups.db'
# def get_db():
#     """
#     function to get database
#     """
#     if 'db' not in g:
#         g.db = StudyGroupDatabase(app.config['DATABASE'])
#     return g.db
###########################################
#### FOR TESTING ####

DATABASE = 'study_groups.db'
# app.config['DATABASE'] = 'study_groups.db'


def get_db():
    """
    function to get database
    """
    if 'db' not in g:
        g.db = StudyGroupDatabase(DATABASE)
    return g.db

##########################################
def get_db():
    db_path = 'study_groups.db'
    return StudyGroupDatabase(db_path)

@app.teardown_appcontext
def close_connection(exception):
    db = g.pop('db', None)
    if db is not None:
        db.close()

# Homepage route
@app.route('/')
def homepage():
    db = get_db()
    users = db.get_users()
    courses = db.search_courses('')
    return render_template('homepage.html', users=users, courses=courses)

#Login Page Route
@app.route("/login", methods=['GET', 'POST'])
def login():
    if 'user_id' in session:
        return redirect(url_for('profile'))
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        db = get_db()
        user_id = db.check_user(email, password)

        if user_id:
            user = User(user_id)
            login_user(user)
            return redirect(url_for('profile'))
        else:
            error = "Invalid email or password. Please try again."
            return render_template('login.html', error=error)

    return render_template('login.html')


# signup page route
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if 'user_id' in session:
        return redirect(url_for('profile'))
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        db = get_db()
        user_id = db.add_user(email, password)
        session['user_id'] = user_id
        return redirect(url_for('profile'))

    # display the signup form
    return render_template('signup.html')


@app.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    db = get_db()
    if request.method == 'POST' and 'search_course_code' in request.form:
        course_code = request.form['search_course_code']
        if db.get_course_by_code(course_code) is not None:
            selected_course = course_code
        else:
            db.add_course(course_code)
            selected_course = course_code

        user_data = db.get_user_data(session['user_id'])
        if user_data is None:
            flash("We will notify you once a match is found.")
            return render_template('profile.html')
        else:
            return render_template('profile.html', user_data=user_data, selected_course=selected_course)

    elif request.method == 'POST':
        name = request.form['name']
        course_code = request.form['course_code']
        meet_days = request.form['meet_days']
        meet_times = request.form['meet_times']
        group_size = request.form['group_size']
        work_style = request.form['work_style']
        goal = request.form['goal']

        db.insert_user_data(session['user_id'], name, course_code,
                            meet_days, meet_times, group_size, work_style, goal)

        matching_users = db.find_matching_users(session['user_id'], course_code, meet_days, meet_times, group_size, work_style, goal)

        if len(matching_users) == 0:
            flash("No match found.")
            return render_template('no_match.html')
        else:
            for match in matching_users:
                match_info = f"{match[0]} ({match[1]}) is looking for a study group for {course_code}. They are available on {meet_days} at {meet_times} with a group size of {group_size}. Their preferred work style is {work_style} and their goal is {goal}."
                notify_match(session['user_id'], match_info)
            return redirect(url_for('profile'))

    else:
        user_data = db.get_user_data(session['user_id'])
        user_preferences = db.get_user_course_preferences(session['user_id'])
        return render_template('profile.html', user_data=user_data, user_preferences=user_preferences)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('homepage'))


if __name__ == '__main__':
    app.run(debug=True)
    get_db()
