from flask import Flask, session, redirect, url_for, render_template

app = Flask(__name__)
app.secret_key = 'your_secret_key'


@app.route('/profile')
def profile():
    if 'username' in session:
        # Show the user's profile
        return render_template('profile.html', username=session['username'])
    else:
        # Redirect to the login page if the user is not logged in
        return redirect(url_for('login'))


@app.route('/logout')
def logout():
    # Clear the user's session
    session.pop('username', None)
    # Redirect to the login page
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Authenticate the user
        username = request.form['username']
        password = request.form['password']
        if username == 'example' and password == 'password':
            # Store the username in the session
            session['username'] = username
            # Redirect to the profile page
            return redirect(url_for('profile'))
        else:
            # Show an error message if the authentication fails
            return render_template('login.html', error='Invalid username or password')
    else:
        # Show the login form
        return render_template('login.html')
