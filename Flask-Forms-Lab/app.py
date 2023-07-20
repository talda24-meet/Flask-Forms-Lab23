from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)


username = "siwarha"
password = "123"
facebook_friends=["Adi","Ilay","Ayoub", "Tal", "Hasan", "Sasha"]


@app.route('/', methods=['GET', 'POST'])  # '/' for the default page
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

@app.route('/home')
def home():
	return render_template('home.html', friends= facebook_friends)

@app.route('/friend_exists/<friend>', methods=['GET', 'POST'])
def friends(facebook_friends):
	exists="False"
	if request.method == 'GET':
		return redirect(url_for('home'))
	else:
		friendInput = request.form['friendChoice']
		for i in facebook_friends:
			if i == friendInput:
				exists="True"
	return render_template('friend_exists.html', exists)	
			
if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
    debug=True
	)
