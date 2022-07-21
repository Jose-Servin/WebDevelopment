from basics import db, Department, Manager, Employee

# CREATING TWO DEPARTMENT OBJECTS
tech = Department('Tech', 5)
AM = Department('Account Manager', 3)

# Adding these two Department instances to the db
db.session.add_all([tech, AM])
db.session.commit()

# Check instances properly added to DB
print(Department.query.all())

# Grab specific instance (This returns a list)
tech = Department.query.filter_by(name='Tech').first()
print(tech)

# Creating Manager for Tech department
tech_manager = Manager('Jose', 'Servin', tech.id)

# Creating Employees for Tech department
emp_1 = Employee('Baker', 'Servin', tech.id)
emp_2 = Employee('Camila', 'Servin', tech.id)

# Commit Manger and new Employees to DB
db.session.add_all([tech_manager, emp_1, emp_2])
db.session.commit()

# Grab tech again after DB updates
tech = Department.query.filter_by(name='Tech').first()
print(tech)

# Show Tech employees
tech.report_employees()
