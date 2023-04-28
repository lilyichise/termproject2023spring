from flask import Flask, render_template, request, g
import sqlite3

app = Flask(__name__)

DATABASE = 'study_groups.db'


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row
    return db


@app.route('/')
def home():
    return render_template('homepage.html')


# Route for the login page
@app.route('/login')
def login():
    return render_template('login.html')


# Route for the signup page
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Do something with the form data
        return redirect(url_for('index'))
    return render_template('signup.html')

@app.route('/index')
def index():
    db = get_db()
    users = db.execute('SELECT * FROM users').fetchall()
    courses = db.execute('SELECT * FROM courses WHERE course_name LIKE ?', ('%math%',)).fetchall()
    return render_template('index.html', users=users, courses=courses)


# Route for the profile page
@app.route('/profile', methods=['GET', 'POST'])
def profile():
    if request.method == 'POST':
        name = request.form['name']
        course_code = request.form['course_code']
        meet_days = request.form['meet_days']
        meet_times = request.form['meet_times']
        group_size = request.form['group_size']
        work_style = request.form['work_style']
        goal = request.form['goal']
        # do something with the form data
    return render_template('profile.html')


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


if __name__ == '__main__':
    app.run(debug=True)
