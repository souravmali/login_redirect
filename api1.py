from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def hame_page():
	return render_template("login.html")

@app.route("/login",methods=['POST'])
def login_page():
	if request.method == 'POST':
		username = request.form['username']
		password = request.form['password']
	
		if username == "sourav" and password == "mali":
			print("login is done")
			return redirect(url_for('product_page'))
					
		else:
			return render_template("error.html")
@app.route("/product")	
def product_page():
	return render_template('product.html')	

if(__name__=="__main__"):
	app.run()
