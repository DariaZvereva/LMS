from lms.app import DB
from uuid import uuid4 as uid


class User(DB.Model):
    id = DB.Column(DB.Integer, primary_key=True)
    username = DB.Column(DB.String(64), index=True, unique=True)
    email = DB.Column(DB.String(120), index=True, unique=True)
    registration_uid = DB.Column(DB.String(64), index=True, unique=True)
    password_hash = DB.Column(DB.String(128))
    name = DB.Column(DB.String(64))
    surname = DB.Column(DB.String(64))
    second_name = DB.Column(DB.String(64))
    student = DB.relationship('student', backref='user', lazy='dynamic', uselist=False)
    teacher = DB.relationship('teacher', backref='user', lazy='dynamic', uselist=False)

    def __repr__(self):
        return '<User {username}, {name} {second_name} {surname}>'.format(username=self.username, name=self.name, second_name=self.second_name,
                                                                          surname=self.surname)

    @staticmethod
    def generate_uid():
        return str(uid())
