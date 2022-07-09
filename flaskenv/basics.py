from flask import Flask, render_template, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, DateTimeField, RadioField, SelectField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey123'


class UserForm(FlaskForm):
    # enter username; check for validation

    username = StringField("Please enter your username: ", validators=[DataRequired()])

    # Booleanfield
    valid_member = BooleanField("Select if you are a member of NLB? ")
    # RadioField
    membership_level = RadioField(
        'Select your membership level: ',
        choices=[
            ('Level_1', 'Level One'),
            ('Level_2', 'Level Two'),
            ('Level_3', 'Level Three')
        ]
    )

    # SelectField
    load_type = SelectField('Type of Load: ',
                            choices=[
                                ('Hot_Loads', 'Hot'),
                                ('Long_Haul', 'Long Haul'),
                                ('Reefer', 'Reefer')
                            ]
                            )
    # comments
    comments = TextAreaField()
    # submit
    submit = SubmitField('Submit')


@app.route('/', methods=['GET', 'POST'])
def index():
    form = UserForm()

    if form.validate_on_submit():
        session['username'] = form.username.data
        session['valid_member'] = form.valid_member.data
        session['membership_level'] = form.membership_level.data
        session['load_type'] = form.load_type.data
        session['comments'] = form.comments.data

        return redirect(url_for('thankyou'))

    return render_template('home.html', form=form)


@app.route('/thankyou', methods=['GET', 'POST'])
def thankyou():
    return render_template('thankyou.html')


if __name__ == '__main__':
    app.run(debug=True)
