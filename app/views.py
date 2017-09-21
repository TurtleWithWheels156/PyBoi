from flask import render_template
from app import app


@app.route("/")
def hello():
    return "Hello World!"

@app.route('/welcome')
def welcome():
    return "Welcome Page!"

@app.route('/temptest')
def templateTest():
    user = {'nickname': 'Jack'} # fake user
    return render_template('index.html',
                           title='Home',
                           user=user)

@app.route('/user/<username>&<int:post_id>')
def show_user_profile(username,post_id):
    #open up page for user info
    return 'User %s is %d' % (username,post_id)
