from lms.app import db


class Teacher(db.Model):
    __tablename__ = None
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
