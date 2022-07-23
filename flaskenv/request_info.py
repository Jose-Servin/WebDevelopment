import os
from request_info_forms import AddForm, DelForm, AddManager
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
    manager = db.relationship('Manager', backref='department', uselist=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        if self.manager:
            return f"Department: {self.name} has assigned manager {self.manager.name}. "
        else:
            return f"Department: {self.name} has no manager assigned yet. "


class Manager(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    # CONNECTING ONE DEPARTMENT WITH ONE MANAGER
    department_id = db.Column(db.Integer, db.ForeignKey('department.id'))

    def __init__(self, name, department_id):
        self.name = name
        self.department_id = department_id

    def __repr__(self):
        return f"Manager: {self.name} works in the Department with ID: {self.department_id}"


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


@app.route('/add_manager', methods=['GET', 'POST'])
def add_manager():
    form = AddManager()

    if form.validate_on_submit():
        manager_name = form.name.data
        manager_dept_id = form.dept_id.data

        # Building Manager instance
        manager_instance = Manager(manager_name, manager_dept_id)

        # Add Manager instance to DB
        db.session.add(manager_instance)
        db.session.commit()
        return redirect(url_for('list_depts'))
    return render_template('request_info_AddManager.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
