import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

login_manager = LoginManager()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey123'
basedir = os.path.abspath(os.path.dirname(__file__))

# SQLALCHEMY CONFIGURATIONS
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# DEFINING DATABASE
db = SQLAlchemy(app)

# MIGRATING APP AND DB
Migrate(app, db)

# this configures our application to have user login management
login_manager.init_app(app)

# This is the view users will go to when logging-in
login_manager.login_view = 'login'
