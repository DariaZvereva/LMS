from wtforms import Form, StringField, PasswordField, validators, IntegerField
from wtforms.validators import DataRequired, ValidationError
from Domain.Users import User

class CourseForm(Form):
    name = StringField('Name', [validators.Length(min=3, max=25)])
    description = StringField('Description', [validators.Length(min=0, max=50)])


class PreliminaryStudentRegForm(Form):
    group_id = StringField('Group', [validators.Length(min=1, max=5)])
    year = IntegerField('Year', [validators.NumberRange(min=1900, max=2016)])
    degree = StringField('Degree', [validators.AnyOf(['bachelor', 'specialist', 'master'])])
    education_form = StringField('Education', [validators.AnyOf(['full', 'part', 'evening'])])
    education_basis = StringField('Education', [validators.AnyOf(['contract', 'budget'])])


class PreliminaryRegForm(Form):
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email Address', [validators.Email(), validators.Length(min=6, max=35)])
    name = StringField('Name', [validators.Length(min=3, max=35)])
    surname = StringField('Surname', [validators.Length(min=3, max=35)])
    second_name = StringField('Surname', [validators.Length(min=3, max=35)])
    password = PasswordField('New Password', [
        validators.DataRequired()
    ])
    status = StringField('Status', [validators.AnyOf(['student', 'teacher', 'admin'])])

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')


class LoginForm(Form):
    email = StringField('email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])