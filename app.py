from flask import Flask, render_template, request
from flask import Flask, g, render_template
from datapase_utils import StudyGroupDatabase
import sqlite3

app = Flask(__name__)

DATABASE = 'study_groups.db'


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        # db = g._database =sqlite3.connect(DATABASE)
        # db.row_factory = sqlite3.Row
        db = g._database = StudyGroupDatabase(DATABASE)
    return db


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@app.route('/')
def index():
    db = get_db()
    # users = db.execute('SELECT * FROM users').fetchall()
    users = db.get_users()
    courses = db.search_courses('math')
    # return render_template('index.html', users=users)
    return render_template('index.html', users=users, courses=courses)


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


if __name__ == '__main__':
    app.run()
