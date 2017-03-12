# File: main.py
# Author: Jacob Hicks 
# GPL 3.0 Licence. See LICENCE for details

# TODO: Figure out how to import @app functions in other files.

# Flask stuff
from flask import *
from flask_login import *
# Database stuff
import sqlite3
# My stuff
import auxlib


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

@app.route('/users/')
@app.route('/users/<name>')
def user(name=None):
    return render_template("user.html", name=name)

@app.route('/test/signup/')
@app.route('/test/signup.html', methods=['GET'])
def adduser():
    return render_template("test-signup.html")

@app.route('/test/signup-success/', methods=['POST', 'GET'])
def signupreturn():
    res = get_db().execute("select firstname from USER where firstname = ?", [request.form['name']])

    if res.fetchone():
        return "User already exists!"
    else:
        print("Query returned: ", res.fetchone())
        get_db().execute("insert into USER values (NULL, ?, ?)", [request.form['name'], request.form['password']])
        get_db().commit()
        return "Test if user is added"

    #return render_template("test-signup-success.html", name=request.form['name'])

@app.errorhandler(404)
def pagenotfound(err):
    return render_template("not_found.html", phrase=auxlib.getRandomPhrase()), 404

# Game demo stuff

@app.route('/test/game.html')
def demogame():
    return render_template('test-game.html')

# Database stuff

@app.route('/admin/createdb/')
def createdb():
    with app.app_context():
        script = open("sql/createtable.sql", "r")
        get_db().executescript(script.read())
        script.close()
        return "Created database!<script>window.location.replace(\"/admin\")</script>"


DATABASE = 'database/datebase.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


app.run()
#app.run(host='0.0.0.0') Don't wanna make the server public right now.
