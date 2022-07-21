from basics import db, Departments

# CREATES ALL THE TABLES, ESSENTIALLY TRANSFORMING MODEL CLASS --> DB.TABLE
db.create_all()

# CREATE DEPARTMENT INSTANCES

Tech = Departments('Tech Team', 5)
AM = Departments('Account Managers', 3)

db.session.add_all([Tech, AM])
db.session.commit()
