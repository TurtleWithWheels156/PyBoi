#TurtleWithWheels15 20176

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/welcome')
def welcome():
    return "Welcome Page!"

@app.route('/user/<username>&<int:post_id>')
def show_user_profile(username,post_id):
    #open up page for user info
    return 'User %s is %d' % (username,post_id)
