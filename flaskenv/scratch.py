from basics import db, Departments, Manager, Employees
from setupdatabase import Tech, AM, CM, Data_Analyst, Customer_Service

all_departments = Departments.query.all()  # returns list of all department objects in the database table
# print(all_departments)

tech_team = Departments.query.filter_by(name='PepsiCo Tech Team')
print(tech_team.all())
Tech.report_employees()
