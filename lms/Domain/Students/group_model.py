from lms.app import DB


class Group(DB.Model):
    id = DB.Column(DB.Integer, primary_key=True)
    name = DB.Column(DB.String(64), index=True, unique=True)
    grade = DB.Column(DB.Integer)
    students = DB.relationship('student', backref='group', lazy='dynamic')

    def __repr__(self):
        return "<Group {}>".format(self.name)
