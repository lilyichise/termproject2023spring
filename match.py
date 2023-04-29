from database_utils import StudyGroupDatabase, creating_database, delete_users_table

def find_matches(database, user_id):
    user_preferences = database.get_user_course_preferences(user_id)
    if user_preferences is None:
        return []

    all_preferences = database.get_all_user_course_preferences()
    matched
