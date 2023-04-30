#########match.py file################
#Finding the matches in the dataset
from app import get_db
from notification_utils import notify_match
from database_utils import StudyGroupDatabase, creating_database, delete_users_table
from notification_utils import notify_match

def find_matches(database, user_id):
    user_preferences = database.get_user_course_preferences(user_id)
    if user_preferences is None:
        return []
    all_preferences = database.get_all_user_course_preferences()
    matched_preferences = []
    for pref in all_preferences:
        if pref != user_preferences and pref not in matched_preferences:
            if len(set(user_preferences) & set(pref)) > 0:
                matched_preferences.append(pref)

                # Notify the user about the match
                notify_match(user_id, pref)

