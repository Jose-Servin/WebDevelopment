from flask import Flask, render_template, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, DateTimeField, RadioField, SelectField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

# Step 1: define app
app = Flask(__name__)

# Step 2: configure secret key
app.config['SECRET_KEY'] = 'mysecretkey123'


# Step 3: Define Form class with attributes; built with wtforms
class InfoForm(FlaskForm):
    # for validators we create an instance in the validators list
    department = StringField('What department are you in? ', validators=[DataRequired()])
    high_access = BooleanField('Do you have level 5 or above access? ')
    # choices in RadioField are a list of Tuple pairs consisting of (value, label)
    access_level = RadioField('Please select your access level: ',
                              choices=[
                                  ('access_5', '5'),
                                  ('access_6', '6'),
                                  ('access_7', '7')
                              ])
    information = SelectField('Please select the information you wish to see: ',
                              choices=[
                                  ('payroll', 'Payroll'),
                                  ('timecard', 'Timecard'),
                                  ('salary', 'Salary'),
                                  ('master_info', 'Master Info')
                              ])

    reason = TextAreaField()
    submit = SubmitField('Submit')


# Step 4: Define view functions
@app.route('/', methods=['GET', 'POST'])
def index():
    # instantiate InfoForm
    form = InfoForm()

    # Only upon submission of form will this be True and user will be redirected to html 'thank_you' renders
    # validate_on_submit will check validators from attribute's; if one is False, user will not be redirected.
    if form.validate_on_submit():
        '''
        In order to pass the data to another template automatically we will use the session object from Flask import.
        Unlike a cookie, session data is stored on the server and a session is just a time interval from when client 
        logs into server and then logs out of it. So the data is stored in a temporary directory on the server. 
        
        This is essentially a way to temporarily hold information about a session that lasted x amount of time for a
        specific user and report it back. 
        
        '''
        # grab session object and treat it as dictionary by building it using dict_value = value from tuple
        session['department'] = form.department.data  # this will report back the value from the tuple pairs
        session['high_access'] = form.high_access.data
        session['access_level'] = form.access_level.data
        session['information'] = form.information.data
        session['reason'] = form.reason.data

        # once the session dictionary is defined use redirect and url_for to redirect to html page on submit
        return redirect(url_for('thankyou'))
    # rendering the Flask_Forms_One_Index.html; this is the page rendered when view function runs
    return render_template('Flask_Forms_One_Index.html', form=form)


@app.route('/thankyou', methods=['GET', 'POST'])
def thankyou():
    return render_template('Flask_Forms_One_ThankYou.html')


if __name__ == "__main__":
    app.run(debug=True)
