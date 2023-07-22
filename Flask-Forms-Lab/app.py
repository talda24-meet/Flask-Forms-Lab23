from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)

username = "siwarha"
password = "123"
facebook_friends = ["Adi", "Ilay", "Ayoub", "Tal", "Hasan", "Sasha"]

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        usernameInput = request.form['username']
        passwordInput = request.form['password']
        if usernameInput == username and passwordInput == password:
            return redirect(url_for('home'))
        else:
            return render_template('login.html')

@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        friend_choice = request.form['friendChoice']
        return redirect(url_for('friend', name=friend_choice))

    return render_template('home.html', friends=facebook_friends)

@app.route('/friend_exists/<name>')
def friend(name):
    exists = name in facebook_friends
    return render_template('friend_exists.html', exists=exists, name=name, friends=facebook_friends)

if __name__ == "__main__":
    app.run(debug=True)
