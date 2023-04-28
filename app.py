import os
from google.auth.transport import requests
from google.oauth2 import id_token
from flask_login import LoginManager, UserMixin, login_user, logout_user, current_user
from flask import Flask, render_template, redirect, url_for, session, request
from database_utils import StudyGroupDatabase

app = Flask(__name__)
app.secret_key = "1234python"
DATABASE = 'study_groups.db'


def get_db():
    if 'db' not in g:
        g.db = StudyGroupDatabase(DATABASE)
    return g.db


@app.teardown_appcontext
def close_connection(exception):
    db = g.pop('db', None)
    if db is not None:
        db.close()


@app.route('/')
def index():
    db = get_db()
    users = db.get_users()
    courses = db.search_courses('math')
    return render_template('homepage.html', users=users, courses=courses)


# Route for the login page
@app.route("/login")
def login():
    return render_template('login.html')


# Route for signup page


@app.route("/signup")
def signup():
    if request.method == 'POST':
        # Do something with the form data
        return redirect(url_for('index'))
    return render_template('signup.html')


@app.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    db = get_db()
    if request.method == 'POST':
        name = request.form['name']
        course_code = request.form['course_code']
        meet_days = request.form['meet_days']
        meet_times = request.form['meet_times']
        group_size = request.form['group_size']
        work_style = request.form['work_style']
        goal = request.form['goal']
        # insert the form data into the database
        db.insert_user_data(session['user_id'], name, course_code,
                            meet_days, meet_times, group_size, work_style, goal)

    user_data = db.get_user_data(session['user_id'])
    return render_template('profile.html', user_data=user_data)


google = oauth.remote_app(
    'google',
    consumer_key='375669104663-n3ocd5qaldera612mnt19cg27i4ar0sq.apps.googleusercontent.com',
    consumer_secret='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',
    request_token_params={
        'scope': 'email'
    },
    base_url='https://www.googleapis.com/oauth2/v1/',
    request_token_url=None,
    access_token_method='POST',
    access_token_url='https://accounts.google.com/o/oauth2/token',
    authorize_url='https://accounts.google.com/o/oauth2/auth',
)


@app.route('/login')
def login():
    return google.authorize(callback=url_for('callback', _external=True))


@app.route('/callback')
def callback():
    access_token = google.authorized_response()['access_token']
    session['access_token'] = access_token
    user_info = requests.get(
        'https://www.googleapis.com/oauth2/v1/userinfo', params={'access_token': access_token})
    return "Hello, {}!".format(user_info.json()['email'])


if __name__ == '__main__':
    app.run(debug=True)
