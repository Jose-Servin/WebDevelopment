from flask import Blueprint

views = Blueprint('views', __name__)  # sets up a Blueprint for our Flask Application


# HOW TO DEFINE VIEW/ROUTE

@views.route('/')
def home():
    return "<h1> TEST </h1>"
