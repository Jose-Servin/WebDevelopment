from flask import Blueprint, render_template, request

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
            pass
        elif len(firstname) < 2:
            pass
        elif password1 != password2:
            pass
        elif len(password1) < 7:
            pass
        else:
            # add user to database
            pass


    return render_template("sign_up.html")
