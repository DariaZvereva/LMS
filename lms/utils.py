import random
import string
from Domain.Users import User
from Domain.Students import Student

def generate_validation_code(N=6):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=N))

def blank_resp():
    return {
        'data': [],
        'error_message': '',
        'status': 'ok'
    }

def get_user_from_form(form):
    return User(
        username=form.username.data,
        email=form.email.data,
        name=form.name.data,
        surname=form.surname.data,
        second_name=form.second_name.data,
        status=form.status.data,
        registration_uid=generate_validation_code()
    )

def get_student_from_form(form, user_id):
    return Student(
        user_id=user_id,
        group_id=form.group_id.data,
        year=form.year.data,
        degree=form.degree.data,
        education_form=form.education_form.data,
        education_basis=form.education_basis.data
    )