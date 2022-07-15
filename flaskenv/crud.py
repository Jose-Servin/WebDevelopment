from basics import db, Departments

## CREATE ##

extra_dept = Departments('Extra Department', 10)
db.session.add(extra_dept)
db.session.commit()

## READ ###
all_departments = Departments.query.all()  # returns list of all department objects in the database table
print(all_departments)

# SELECT BY ID
department_id_1 = Departments.query.get(1)  # This returns the Object with ID 1
print(department_id_1.name)  # this prints out the specific attribute of that object returned

# FILTER (THIS PRODUCES SQL CODE FOR US)
AM_dept = Departments.query.filter_by(name='Account Managers')
print(AM_dept.all())

### UPDATE
first_dept = Departments.query.get(1)
first_dept.security_level = 7
db.session.add(first_dept)  # adding back in the edited Department object
db.session.commit()

#### DELETE
dept_to_del = Departments.query.get(6)
db.session.delete(dept_to_del)
db.session.commit()

## Check changes
all_departments = Departments.query.all()
print(all_departments)
