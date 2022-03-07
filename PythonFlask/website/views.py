from flask import Blueprint, render_template

views = Blueprint('views', __name__)  # sets up a Blueprint for our Flask Application


# HOW TO DEFINE VIEW/ROUTE

@views.route('/')
def home():
    return render_template("home.html")
