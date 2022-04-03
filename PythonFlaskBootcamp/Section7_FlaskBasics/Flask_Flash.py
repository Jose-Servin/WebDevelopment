from flask import Flask, render_template, flash, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey123'


class SimpleForm(FlaskForm):
    submit = SubmitField('Submit')
    department = StringField('Enter your department: ')


@app.route('/', methods=['GET', 'POST'])
def index():
    form = SimpleForm()

    if form.validate_on_submit():
        session['department'] = form.department.data
        flash(f"Your department is {session['department']}")

        return redirect(url_for('index'))

    return render_template('Flask_Flash_Index.html', form=form)


if __name__ == "__main__":
    app.run(debug=True)
