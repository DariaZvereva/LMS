from lms.app import db


class Course(db.Model):
    __tablename__ = "courses"
    __table_args__ = {"extend_existing": True}
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, index=True)
    description = db.Column(db.String(64))

    def __repr__(self):
        return '<Course {name}>'.format(name=self.name)

    def get_id(self):
        return self.id

