from flask import Flask, render_template, request
import re

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/report')
def report():
    username = request.args.get('username')

    has_uppercase = False
    has_lowercase = False
    has_number = False

    has_uppercase = any(i.isupper() for i in username)
    has_lowercase = any(i.islower() for i in username)
    has_number = username[-1].isdigit()

    valid_username = has_number and has_uppercase and has_lowercase

    return render_template('signup.html', valid_username=valid_username, has_number=has_number,
                           has_lowercase=has_lowercase,
                           has_uppercase=has_uppercase)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404_error.html'), 404


if __name__ == '__main__':
    app.run(debug=True)
