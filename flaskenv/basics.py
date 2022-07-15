import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

basedir = os.path.abspath(os.path.dirname(__file__))
# __file__ --> basics.py
# the os.path.dirname is flaskenv/basics.py
# the abspath is the "full path" which when printed is /Users/joseservin/WebDevelopment/flaskenv

# CREATING FLASK APP
app = Flask(__name__)

# SQLALCHEMY CONFIGURATIONS
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# DEFINING DATABASE
db = SQLAlchemy(app)

# MIGRATING APP AND DB
Migrate(app, db)


# HOW TO CREATE A MODEL
class Departments(db.Model):
    # create columns for table
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    security_level = db.Column(db.Integer)
    incentive = db.Column(db.BOOLEAN)

    def __init__(self, name, security_level, incentive):
        self.name = name
        self.security_level = security_level
        self.incentive = incentive

    def __repr__(self):
        rep = f"The {self.name} has a security level of {self.security_level}. Incentive? {self.incentive} "
        return rep
