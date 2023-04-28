from flask import Flask, render_template, redirect, url_for, session, request
from datapase_utils import StudyGroupDatabase

app = Flask(__name__)
app.secret_key = "super_secret_key"

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


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/signup')
def signup():
    return render_template('signup.html')


@app.route('/google_login')
def google_login():
    # handle Google sign-in logic here
    # set session variables as needed
    return redirect(url_for('profile'))


@app.route('/google_signup')
def google_signup():
    # handle Google sign-up logic here
    # set session variables as needed
    return redirect(url_for('profile'))


@app.route('/profile', methods=['GET', 'POST'])
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


if __name__ == '__main__':
    app.run(debug=True)
