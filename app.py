from flask import Flask, g, render_template
import sqlite3

app = Flask(__name__)

DATABASE = 'study_groups.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database =sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route('/')
def index():
    db = get_db()
    users = db.execute('SELECT * FROM users').fetchall()
    return render_template('index.html', users=users)