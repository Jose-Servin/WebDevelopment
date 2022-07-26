from flask import Blueprint, render_template, redirect, url_for
from myproject import db
from myproject.models import Manager
from myproject.managers.forms import AddForm

manager_blueprint = Blueprint('manager', __name__, template_folder='templates/managers')


@manager_blueprint.route('/add', methods=['GET', 'POST'])
def add():
    form = AddForm()

    if form.validate_on_submit():
        manager_name = form.name.data
        manager_dept_id = form.dept_id.data

        # Building Manager instance
        manager_instance = Manager(manager_name, manager_dept_id)

        # Add Manager instance to DB
        db.session.add(manager_instance)
        db.session.commit()
        return redirect(url_for('department.list_depts'))
    return render_template('add_manager.html', form=form)
