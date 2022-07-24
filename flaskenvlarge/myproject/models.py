# set up db inside the __init__.py file under myproject folder
from flaskenvlarge.myproject import db


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
