from flask import Flask, request, render_template

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

@app.route('/user/<name>')
def user(name):
    return render_template("user.html", name=name)

@app.errorhandler(404)
def pagenotfound(err):
    return render_template("not_found.html"), 404

app.run()
