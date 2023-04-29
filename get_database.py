from database_utils import StudyGroupDatabase

# create an instance of the StudyGroupDatabase class
db = StudyGroupDatabase('study_groups.db')

# retrieve all users from the database
users = db.get_users()

# print the results
for user in users:
    print(user)
