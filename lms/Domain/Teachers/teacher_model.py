from lms.app import DB


class Teacher(DB.Model):
    id = DB.Column(DB.Integer, primary_key=True)
    user_id = DB.Column(DB.Integer, DB.ForeignKey('user.id'))

    def key(self):
        return self.id
