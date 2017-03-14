# File: main.py
# Author: Jacob Hicks 
# GPL 3.0 Licence. See LICENCE for details

# TODO: Figure out how to import @app functions in other files.

# Flask stuff
from flask import *
from flask_login import *
# Database stuff
import sqlite3
# stdlib stuff
import os
# My stuff
import auxlib
import database

app = Flask(__name__)

@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html')

#   TODO:
#   Actually verify if user is an admin
#   Add commands to admin page: createdb, ban user, disable signup, delete user, etc
@app.route('/admin/')
@app.route('/admin.html')
def admin(is_admin=False):
    return render_template('admin.html', is_admin=is_admin)

@app.route('/signup/')
@app.route('/signup.html')
def signup():
    return render_template("signup.html")

@app.route('/play')
@app.route('/play.html')
def play():
    return render_template("play.html")

#@app.route('/users/')
@app.route('/users/<name>')
def user(name=None):
    res = database.get_db().execute("select * from USER where firstname = ?", [name])
    res = res.fetchone()[1] # Index one is the username
    if res:
        return render_template("user.html", name=res)
    else:
        return render_template("user.html", name=None)

@app.route('/signup-result/', methods=['POST', 'GET'])
def signupreturn():
    res = database.get_db().execute("select firstname from USER where firstname = ?", [request.form['name']])
    # Re-type the result to be the name given by the user.
    res = res.fetchone()
    # If the user is already in the database
    if res:
        print("Returned existing: ", res)
        return "User already exists!"
    # Otherwise add them, add their password, and thank them :)
    else:
        print("Creating new user: ", request.form['name'])
        database.get_db().execute("insert into USER (firstname, password, isadmin) values (?, ?, 0)", [request.form['name'], request.form['password']])
        database.get_db().commit()
        return "Thank you for signing up!"

@app.errorhandler(404)
def pagenotfound(err):
    return render_template("not_found.html", phrase=auxlib.getRandomPhrase()), 404
    
database.init_db_dir()
app.run()