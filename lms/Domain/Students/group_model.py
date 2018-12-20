from lms.app import db


class Group(db.Model):
    __tablename__ = "groups"
    __table_args__ = {"useexisting": True}
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    department = db.String(64)
    grade = db.Column(db.Integer)
    students = db.relationship('Student', backref='group', lazy='dynamic')

    def __repr__(self):
        return "<Group {}>".format(self.name)

    def get_id(self):
        return self.id
