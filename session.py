from flask import Flask, request, render_template, redirect, url_for,session

app = Flask(__name__)
app.secret_key = 'any random string'

@app.route('/')
def index():
	if("username" in session.keys()):
		return render_template("login.html", login="True")
	
	else:
		return render_template("login.html", login="False")
		

@app.route("/login",methods=['POST'])
def login_page():
	if request.method == 'POST':
		username = request.form['username']
		password = request.form['password']
	
		if username == "sourav" and password == "mali":
			print("login is done")
			session['username'] = request.form["username"]
			return redirect(url_for('index'))
					
		else:
			return render_template("error.html")
@app.route("/product")	
def product_page():
	return render_template('product.html')	

@app.route('/logout')
def logout():

	session.pop('username',None)
	return redirect(url_for('index'))
	
if(__name__=="__main__"):
	app.run()
