# Section 9: Forms with Flask
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

# Step 1: create application
app = Flask(__name__)

# Step 2: configure secret key to use with CSRF (cross-site request forgery)
app.config['SECRET_KEY'] = 'mysecretkey123'


# Step 3: create WTF Form class
# inherit from FlaskForm
class InfoForm(FlaskForm):
    # define class attributes
    department = StringField("What department do you work in? ")
    submit = SubmitField("Submit")


# Step 4: create view function that creates instance of WTF form class and checks if it's a valid submission
@app.route('/', methods=['GET', 'POST'])
def index():
    # set department variable equal to False, different from the department attribute defined in our class
    department = False
    # create instance of our form
    form = InfoForm()

    if form.validate_on_submit():
        # grab department from form (grabs data submitted for this attribute)
        department = form.department.data
        # reset this attribute to an empty string
        form.department.data = ''

    return render_template('Flask_Forms_Index.html', form=form, department=department)


if __name__ == '__main__':
    app.run(debug=True)
