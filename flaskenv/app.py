from user_auth import app, db
from flask import render_template, redirect, request, url_for, flash, abort
from flask_login import login_user, login_required, logout_user
from user_auth.models import User
from user_auth.forms import LoginForm, RegistrationForm


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/welcome')
@login_required
def welcome_user():
    return render_template('welcome_user.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have logged out!')
    return redirect(url_for('home'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        # grab user from DB
        user = User.query.filter_by(email=form.email.data).first()

        if user.check_password(form.password.data) and user is not None:
            # this is saying "if a user was created and if the password matches the hash"""
            login_user(user)
            flash('Logged in Successfully!')

            # Flask Login Part 3: 12 min mark
            next_action = request.args.get('next')
            if next_action is None or not next_action[0] == '/':
                next_action = url_for('welcome_user')
            return redirect(next_action)
    return render_template('login.html', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        user = User(email=form.email.data,
                    username=form.username.data,
                    password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Thank you for registering!')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
