from lms.app import DB


class Course(DB.Model):
    id = DB.Column(DB.Integer, primary_key=True)
    name = DB.Column(DB.String(64), unique=True, index=True)
    description = DB.Column(DB.String(64))

    def __repr__(self):
        return '<Course {course_id}, {name} {description}>'.format(course_id=self.course_id, name=self.name, description=self.description)
