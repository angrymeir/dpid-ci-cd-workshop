# flask app serving a web interface with user authentication

from flask import Flask, render_template, request, redirect, url_for

from flask import session as login_session

import requests
import os

os.system('ls')


app = Flask(__name__)
app.debug = True
app.secret_key = 'verysecretkey'
app.config['SESSION_TYPE'] = 'filesystem'

@app.route('/default', methods=['GET'])
def default():
    if login_session.get('username') is None:
        return redirect(url_for('login'))
    return render_template('default.html')

@app.route('/', methods=['GET', 'POST'])
def login():
    if login_session.get('username') is not None:
            return redirect(url_for('default'))
    # check if request is valid
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # check if username and password are correct
        if username == 'admin' and password == 'admin':
            # create a session token
            login_session['username'] = username
            return redirect(url_for('default'))
        else:
            # invalid username or password
            return redirect(url_for('login'))
    return render_template('login.html')

@app.route('/logout', methods=['GET'])
def logout():
    if login_session.get('username') is not None:
        login_session.pop('username', None)
    return redirect(url_for('login'))