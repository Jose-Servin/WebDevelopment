import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# CREATING FLASK APP
app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'

basedir = os.path.abspath(os.path.dirname(__file__))

# SQLALCHEMY CONFIGURATIONS
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# DEFINING DATABASE
db = SQLAlchemy(app)

# MIGRATING APP AND DB
Migrate(app, db)
