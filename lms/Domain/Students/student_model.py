from lms.app import DB


class Student(DB.Model):
    id = DB.Column(DB.Integer, primary_key=True)
    user_id = DB.Column(DB.Integer, DB.ForeignKey('user.id'))
    group_id = DB.Column(DB.Integer, DB.ForeignKey('group.id'))
    year = DB.Column(DB.Integer)
    degree = DB.Column(DB.String(64))
    education_form = DB.Column(DB.String(64))
    is_contract = DB.Column(DB.Boolean)

    def __repr__(self):
        return '<Student {user_id}, {education_form} {group_id} {degree}>'.format(user_id=self.user_id, education_form=self.education_form,
                                                                                  group_id=self.group_id,
                                                                                  degree=self.degree)
