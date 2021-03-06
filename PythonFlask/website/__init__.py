from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()
DB_NAME = 'database.db'


def create_app():
    app = Flask(__name__)  # needed as a default setup for Flask
    app.config['SECRET_KEY'] = 'BakerCamilaBella'
    app.config['SQLALCHEMY_DATABASE_URL'] = f"sqlite:///{DB_NAME}"
    db.init_app(app)

    # IMPORTING BLUEPRINTS TO __INIT__ FILE
    from .views import views
    from .auth import auth

    # REGISTER BLUEPRINTS WITH OUT FLASK APPLICATION
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Note

    return app

def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print("Created Database!")
