from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)  # sets up a Blueprint for our Flask Application


@auth.route('/login', methods=['GET','POST'])
def login():
    return render_template("login.html", text="Test", boolean=True)


@auth.route('/logout')
def logout():
    return "<p> Logout </p>"


@auth.route('/sign-up',methods=['GET','POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstname = request.form.get('firstname')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4:
            flash('Email must be greater than 3 characters', category="error")
        elif len(firstname) < 2:
            flash('First name must be greater than 1 character', category="error")
        elif password1 != password2:
            flash('Passwords do not match', category="error")
        elif len(password1) < 7:
            flash('Password must be at least 7 characters', category="error")
        else:
            # add user to database
            flash('Account created!', category="success")

    return render_template("sign_up.html")
