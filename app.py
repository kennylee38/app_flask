from flask import Flask
from markupsafe import escape
app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'
@app.route('/about')
def about():
    return 'This is an about page :)'
@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % escape(username)