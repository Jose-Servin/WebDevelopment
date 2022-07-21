import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

basedir = os.path.abspath(os.path.dirname(__file__))
# __file__ --> basics.py
# the os.path.dirname is flaskenv/basics.py
# the abspath is the "full path" which when printed is /Users/joseservin/WebDevelopment/flaskenv

# CREATING FLASK APP
app = Flask(__name__)

# SQLALCHEMY CONFIGURATIONS
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# DEFINING DATABASE
db = SQLAlchemy(app)

# MIGRATING APP AND DB
Migrate(app, db)


# HOW TO CREATE A MODEL
class Department(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    security_level = db.Column(db.Integer)
    # ONE-TO-MANY RELATIONSHIP (ONE DEPARTMENT CAN HAVE MANY EMPLOYEES)
    employees = db.relationship('Employee', backref='department', lazy='dynamic')

    # ONE-TO-ONE RELATIONSHIP (ONE DEPARTMENT HAS ONE MANAGER)
    manager = db.relationship('Manager', backref='department', uselist=False)

    def __init__(self, name, security_level):
        self.name = name
        self.security_level = security_level

    def __repr__(self):
        if self.manager:
            return f"Department name: {self.name} | Manager {self.manager.first_name} {self.manager.last_name}"
            # self.manager.name is an attribute from the Manager class
        else:
            return f"{self.name} department has no Manager assigned. "

    def report_employees(self):
        print(f"{self.name} department has these employees: ")
        for employee in self.employees:
            print(f"{employee.first_name} {employee.last_name}")  # this is an attribute from the Employees class


class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.Text)
    last_name = db.Column(db.Text)

    # CONNECTING EMPLOYEES WITH DEPARTMENTS
    department_id = db.Column(db.Integer, db.ForeignKey('department.id'))

    def __init__(self, first_name, last_name, department_id):
        self.first_name = first_name
        self.last_name = last_name
        self.department_id = department_id

    def __repr__(self):
        return f"Employee: {self.first_name} {self.last_name} works in Department ID {self.department_id}"


class Manager(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.Text)
    last_name = db.Column(db.Text)

    # CONNECTING ONE DEPARTMENT WITH ONE MANAGER
    department_id = db.Column(db.Integer, db.ForeignKey('department.id'))

    def __init__(self, first_name, last_name, department_id):
        self.first_name = first_name
        self.last_name = last_name
        self.department_id = department_id

    def __repr__(self):
        return f"Manager: {self.first_name} {self.last_name} works in Department ID {self.department_id}"
