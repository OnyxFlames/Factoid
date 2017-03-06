from flask import Flask, request, render_template

import sqlite3
from flask import g

app = Flask(__name__)

@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/admin/')
@app.route('/admin.html')
def admin():
    return render_template('admin.html')

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
@app.route('/test/signup.html')
def adduser():
    return render_template("test-signup.html")

@app.errorhandler(404)
def pagenotfound(err):
    return render_template("not_found.html"), 404

# Database stuff

@app.route('/admin/createdb/')
def createdb():
    with app.app_context():
        get_db().execute("create table if not exists USER (id INT IDENTITY, firstname varchar(25),"
                         " lastname varchar(30), constraint pk_id_constraint PRIMARY KEY(id));")
    return "<h1>Admin Control Panel</h1>"

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
