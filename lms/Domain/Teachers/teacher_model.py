from lms.app import db


class Teacher(db.Model):
    __tablename__ = "teachers"
    __table_args__ = {"useexisting": True}
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
