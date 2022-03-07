from flask import Flask


def create_app():
    app = Flask(__name__)  # needed as a default setup for Flask
    app.config['SECRET_KEY'] = 'BakerCamilaBella'

    # IMPORTING BLUEPRINTS TO __INIT__ FILE
    from .views import views
    from .auth import auth

    # REGISTER BLUEPRINTS WITH OUT FLASK APPLICATION
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')


    return app
