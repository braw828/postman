from db_setup import init_db
from app import app
from flask import render_template, request, Flask



@app.route('/login', methods=['GET'])
def login_page():
	return render_template("login_page.html")

if __name__  == "__main__":
	app.run()
