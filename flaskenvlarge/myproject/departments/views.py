from flask import Blueprint, render_template, redirect, url_for
from myproject import db
from myproject.models import Department
from myproject.departments.forms import AddForm, DelForm

department_blueprint = Blueprint('department', __name__, template_folder='templates/departments')


@department_blueprint.route('/add', methods=['GET', 'POST'])
def add():
    form = AddForm()
    if form.validate_on_submit():
        # Grab info provided by user
        dept_name = form.name.data
        # Create Table instance
        new_dept = Department(dept_name)
        # DB interaction
        db.session.add(new_dept)
        db.session.commit()
        return redirect(url_for('department.list_depts'))

    else:
        return render_template('add.html', form=form)


@department_blueprint.route('/list')
def list_depts():
    all_departments = Department.query.all()
    return render_template('list.html', all_departments=all_departments)


@department_blueprint.route('/delete', methods=['GET', 'POST'])
def delete():
    form = DelForm()
    if form.validate_on_submit():
        dept_id = form.id.data
        dept = Department.query.get(dept_id)
        db.session.delete(dept)
        db.session.commit()
        return redirect(url_for('department.list_depts'))

    else:
        return render_template('delete.html', form=form)
