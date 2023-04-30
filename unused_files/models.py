from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone_number = db.Column(db.String(20))
    password = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return f"<User {self.name}>"

class Course(db.Model):
    __tablename__ = 'courses'
    course_id = db.Column(db.Integer, primary_key=True)
    course_name = db.Column(db.String(120), nullable=False)
    course_code = db.Column(db.String(20), unique=True, nullable=False)

    def __repr__(self):
        return f"<Course {self.course_code}>"

class UserCourse(db.Model):
    __tablename__ = 'user_courses'
    user_course_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('courses.course_id'), nullable=False)
    preferred_days = db.Column(db.String(120), nullable=False)
    preferred_times = db.Column(db.String(120), nullable=False)
    group_size_preference = db.Column(db.String(20), nullable=False)
    work_style = db.Column(db.String(50), nullable=False)
    goal = db.Column(db.String(120), nullable=False)

    user = db.relationship("User", backref="user_courses")
    course = db.relationship("Course", backref="user_courses")

    def __repr__(self):
        return f"<UserCourse {self.user_id} {self.course_id}>"
