from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/admin.html')
def admin():
    return render_template('admin.html')


app.run()
