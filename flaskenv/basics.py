from flask import Flask, render_template, flash, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

# Next we set up our application and security key:
app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey123'


# We move on to creating a simple form.
class SimpleForm(FlaskForm):
    department = StringField('What department are you in? ')
    submit = SubmitField('Submit')


# here we define our index view function

@app.route('/', methods=['GET', 'POST'])
def index():
    form = SimpleForm()

    if form.validate_on_submit():
        session['department'] = form.department.data
        flash(f"You are in the {session['department']} department. ")

        return redirect(url_for('index'))

    return render_template('home.html', form=form)


if __name__ == "__main__":
    app.run(debug=True)
