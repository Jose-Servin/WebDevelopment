from flask import Blueprint

auth = Blueprint('auth', __name__)  # sets up a Blueprint for our Flask Application


@auth.route('/login')
def login():
    return "<p> Login </p>"


@auth.route('/logout')
def logout():
    return "<p> Logout </p>"


@auth.route('/sign-up')
def sign_up():
    return "<p> Sign Up </p>"
