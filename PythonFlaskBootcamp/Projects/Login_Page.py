from flask import Flask, render_template, request
from flask import Flask, render_template, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, DateTimeField, RadioField, SelectField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

# Step 1: define app
app = Flask(__name__)

# Step 2: configure secret key
app.config['SECRET_KEY'] = 'mysecretkey12'


# Step 3: Define Form class with attributes; built with wtforms


# Step 4: Define view functions

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('Login_Page_Index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('Login_Page_Username_Password.html')


if __name__ == "__main__":
    app.run(debug=True)
