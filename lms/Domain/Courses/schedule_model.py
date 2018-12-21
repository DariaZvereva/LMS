from lms.app import db
from lms.Domain.Students import Group
from lms.Domain.Courses import Course


class Schedule(db.Model):
    __tablename__ = "schedule"
    __table_args__ = {"extend_existing": True}
    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'))
    group_id = db.Column(db.Integer, db.ForeignKey('groups.id'))

    def __repr__(self):
        return '| {course} - {group} |'.format(
            course=self.get_course(), group=self.get_group()
        )

    def get_group(self):
        return Group.query.filter_by(id=self.group_id).first()

    def get_course(self):
        return Course.query.filter_by(id=self.course_id).first()
