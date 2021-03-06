from lms.app import db


class Teacher(db.Model):
    __tablename__ = "teachers"
    __table_args__ = {"extend_existing": True}
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
