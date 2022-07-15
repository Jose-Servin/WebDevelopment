from basics import db, Departments

# CREATES ALL THE TABLES, ESSENTIALLY TRANSFORMING MODEL CLASS --> DB.TABLE
db.create_all()

# CREATE DEPARTMENT INSTANCES

Tech = Departments('PepsiCo Tech Team', 5)
AM = Departments('Account Managers', 3)
CM = Departments('Carrier Managers', 3)
Data_Analyst = Departments('Data Analyst', 8)
Customer_Service = Departments('Customer Service', 1)

db.session.add_all([Tech, AM, CM, Data_Analyst, Customer_Service])
db.session.commit()

# print(Tech.id)
# print(AM.id)


# CHECK DATA INSERTION TO DB WAS SUCCESSFUL
# print(Departments.query.all())
