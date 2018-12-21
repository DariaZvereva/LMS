import random
import string
import json
from flask import Response
from lms.Domain.Users import User
from lms.Domain.Students import Student

def get_response(answer):
    answer_js = json.dumps(answer)
    if answer.get('status') == 'error':
        return Response(answer_js, status=400, mimetype='application/json')
    return Response(answer_js, status=200, mimetype='application/json')

def generate_validation_code(string_length=6):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=string_length))

def blank_resp():
    return {
        'data': [],
        'error_message': '',
        'status': 'ok'
    }

def init_user(form):
    return User(
        name=form.name.data,
        surname=form.surname.data,
        second_name=form.second_name.data,
        status=form.status.data,
        registration_uid=generate_validation_code()
    )

def init_student(form, user_id, group_id):
    return Student(
        user_id=user_id,
        group_id=group_id,
        year=form.year.data,
        degree=form.degree.data,
        education_form=form.education_form.data,
        education_basis=form.education_basis.data
    )

def init_full_user(form):
    user = User(
        name=form.name.data,
        surname=form.surname.data,
        second_name=form.second_name.data,
        status=form.status.data,
        registration_uid=generate_validation_code(),
        email=form.email.data,
        username=form.username.data
    )
    user.set_password(form.password.data)
    return user
