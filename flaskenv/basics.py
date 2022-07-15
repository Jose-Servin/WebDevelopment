import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))
# __file__ --> basics.py
# the os.path.dirname is flaskenv/basics.py
# the abspath is the "full path" which when printed is /Users/joseservin/WebDevelopment/flaskenv

# 1. Create Flask App
app = Flask(__name__)

# 2. Configure Flask App for SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join((basedir, 'data.sqlite'))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 3. Pass our application into SQLAlchemy class call

db = SQLAlchemy(app)


# HOW TO CREATE A MODEL
class Departments(db.Model):
    # create columns for table
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    security_level = db.Column(db.Integer)

    def __init__(self, name, security_level):
        self.name = name
        self.age = security_level

    def __repr__(self):
        rep = f"The {self.name} has a security level of {self.security_level}. "
        return rep
