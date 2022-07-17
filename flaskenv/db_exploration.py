from basics import db, Departments, Manager, Employees
from setupdatabase import Tech, AM, CM, Data_Analyst, Customer_Service

all_departments = Departments.query.all()  # returns list of all department objects in the database table
print(all_departments)

# Tech Team before Manager is assigned
tech_team = Departments.query.filter_by(name='PepsiCo Tech Team')
print(tech_team)

# CREATING A MANAGER FOR THE TECH TEAM
tech_manager = Manager('Bob', 'Smith', Tech.id)

# CREATING 2 EMPLOYEES FOR THE TECH TEAM
employee_1 = Employees('Jose', 'Servin', Tech.id)
employee_2 = Employees('Baker', 'Servin', Tech.id)

# Adding Manager and Employees instances created to our DB
db.session.add_all([tech_manager, employee_1, employee_2])
db.session.commit()

# Check Tech Team __repr__ method to see Manager was assigned
tech_team = Departments.query.filter_by(name='PepsiCo Tech Team')
print(tech_team)

# Check Tech Team employees
Tech.report_employees()
