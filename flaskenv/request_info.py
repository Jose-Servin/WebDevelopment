import os
from request_info_forms import AddForm, DelForm
from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'

###############################
### Setting up SQL Database ###
###############################

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
Migrate(app, db)


###############################
########## Models #############
###############################

class Department(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Department: {self.name}"


###############################
####### View Function #########
###############################

@app.route('/')
def index():
    return render_template('request_info_home.html')


@app.route('/add', methods=['GET', 'POST'])
def add_department():
    form = AddForm()
    if form.validate_on_submit():
        # Grab info provided by user
        dept_name = form.name.data
        # Create Table instance
        new_dept = Department(dept_name)
        # DB interaction
        db.session.add(new_dept)
        db.session.commit()
        return redirect(url_for('list_depts'))

    else:
        return render_template('request_info_add.html', form=form)


@app.route('/list')
def list_depts():
    all_departments = Department.query.all()
    return render_template('request_info_list.html', all_departments=all_departments)


@app.route('/remove', methods=['GET', 'POST'])
def delete_department():
    form = DelForm()
    if form.validate_on_submit():
        dept_id = form.id.data
        dept = Department.query.get(dept_id)
        db.session.delete(dept)
        db.session.commit()
        return redirect(url_for('list_depts'))

    else:
        return render_template('request_info_delete.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
