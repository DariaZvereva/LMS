from lms.app import db
from lms.Domain.Students import Group


class Student(db.Model):
    __tablename__ = "students"
    __table_args__ = {"extend_existing": True}
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    group_id = db.Column(db.Integer, db.ForeignKey('groups.id'))
    year = db.Column(db.Integer)
    degree = db.Column(db.String(64))
    education_form = db.Column(db.String(64))
    education_basis = db.Column(db.String(64))

    def __repr__(self):
        return 'User_id: {user_id}, Учебная группа: {group}, ' \
                'Год поступления: {year}, Степень: {degree}, ' \
               'Форма обучения: {education}, Основа обучения: {basis} |'.format(
                   group=self.get_group(), year=self.year,
                   degree=self.degree, education=self.education_form,
                   basis=self.education_basis, user_id=self.user_id)

    def get_group(self):
        return Group.query.filter_by(id=self.group_id).first()

    def get_group_id(self):
        return self.group_id

    def get_id(self):
        return self.id
