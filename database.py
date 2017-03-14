# https://docs.python.org/3/tutorial/modules.html

import sqlite3

DATABASEDIR = 'database/'

DATABASEFILE = 'datebase.db'

DATABASE = DATABASEDIR + DATABASEFILE

from flask import *
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

import os
def init_db_dir():
    if (not os.path.exists(DATABASEDIR)):
        mkdir(DATABASEDIR)

    if(not os.path.isfile(DATABASE)):
        with app.app_context():
            script = open("sql/createtable.sql", "r")
            get_db().executescript(script.read())
            script.close()
            print("Initial run. Database created at: ", DATABASE)

from main import app
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

del app
