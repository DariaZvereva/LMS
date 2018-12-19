from lms.app import db


class Student(db.Model):
    __tablename__ = "students"
    __table_args__ = {"useexisting": True}
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    group_id = db.Column(db.Integer, db.ForeignKey('groups.id'))
    year = db.Column(db.Integer)
    degree = db.Column(db.String(64))
    education_form = db.Column(db.String(64))
    is_contract = db.Column(db.Boolean)
