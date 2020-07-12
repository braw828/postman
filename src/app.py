# app.py

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres:nevermind@localhost/int0'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['FLASK_DEBUG'] = True
app.config['TESTING'] =  True
app.secret_key = 'hhdfhfsksdkjfkjs#dsgsd#@3SAD'
app.flask_debug = True

db = SQLAlchemy(app)
