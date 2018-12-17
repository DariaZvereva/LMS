import json
from flask import Flask, request, Response
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager,\
    current_user, login_user, logout_user, login_required

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)

from utils import blank_resp, get_user_from_form, get_student_from_form
from forms import PreliminaryRegForm, PreliminaryStudentRegForm, LoginForm, CourseForm
from Domain.Users import User
from Domain.Courses import Course
from Domain.Students import Student, Group
from Domain.Teachers import Teacher


def add_course_in(form):
    course = Course(name=form.name.data, description=form.name.data)
    db.session.add(course)
    db.session.commit()

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/preliminary_register', methods=['POST'])
# @login_required
def preliminary_register_user():
    """Администратор может добавить предопределенного пользователя (студента или преподавателя)

    """
    answer = blank_resp()

    try:
        form = PreliminaryRegForm(request.form)
        if form.validate():
            user = get_user_from_form(form)
            user.set_password(form.password.data)

            db.session.add(user)
            db.session.commit()

            if user.get_status() == 'student':
                form_student = PreliminaryStudentRegForm(request.form)
                if form_student.validate():
                    user_id = user.get_user_id()
                    student = get_student_from_form(form_student, user_id)
                    db.session.add(student)
                    db.session.commit()
                else:
                    db.session.delete(user)
                    db.session.commit()
                    raise Exception(str(form_student.errors.items()))

        else:
            raise Exception(str(form.errors.items()))

    except Exception as e:
        answer['status'] = 'error'
        answer['error_message'] = str(e)

    js = json.dumps(answer)
    resp = Response(js, status=200, mimetype='application/json')
    return resp


@app.route('/login', methods=['GET', 'POST'])
def login():
    """Пользователь может войти в систему по своему e-mail и паролю.

    """
    answer = blank_resp()

    try:
        if current_user.is_authenticated:
            raise Exception('User is already authenticated')
        form = LoginForm(request.form)
        if form.validate():
            user = User.query.filter_by(email=form.email.data).first()
            if user is None or not user.check_password(form.password.data):
                raise Exception('Invalid username or password')
            login_user(user)
        else:
            raise Exception(str(form.errors.items()))

    except Exception as e:
        answer['status'] = 'error'
        answer['error_message'] = str(e)

    js = json.dumps(answer)
    resp = Response(js, status=200, mimetype='application/json')
    return resp

@app.route('/logout')
def logout():
    answer = blank_resp()
    try:
        logout_user()
    except Exception as e:
        answer['status'] = 'error'
        answer['error_message'] = str(e)

    js = json.dumps(answer)
    resp = Response(js, status=200, mimetype='application/json')
    return resp


@app.route('/user/<username>', methods=['GET', 'POST'])
@login_required
def user(username):
    """Пользователь может просмотреть (GET) и отредактировать (POST) свой профиль

    """
    answer = blank_resp()

    try:
        if request.method == 'GET':
            user = User.query.filter_by(username=username).first_or_404()
            answer['data'] = user.get_data()
    except Exception as e:
        answer['status'] = 'error'
        answer['error_message'] = str(e)

    js = json.dumps(answer)
    resp = Response(js, status=200, mimetype='application/json')
    return resp


@app.route('/create_course', methods=['GET', 'POST'])
@login_required
def create_course():
    """ Администратор может создать учебный курс, указав его название и текстовое описание.

    """
    answer = blank_resp()

    form = CourseForm(request.form)
    if form.validate():
        add_course_in(form)
    else:
        answer['status'] = 'error'
        answer['error_message'] = str(form.errors.items())

    js = json.dumps(answer)
    resp = Response(js, status=200, mimetype='application/json')
    return resp


# TODO: дублирование кода: переделать
@app.route('/get_all', methods=['GET'])
def get_all():
    answer = blank_resp()

    try:
        type = request.args.get('type')
        if type == 'users':
            answer['data'] = str(User.query.all())
        elif type == 'courses':
            answer['data'] = str(Course.query.all())
        elif type == 'students':
            answer['data'] = str(Student.query.all())
        else:
            raise Exception('Invalid type')
    except Exception as e:
        answer['status'] = 'error'
        answer['error_message'] = str(e)

    js = json.dumps(answer)
    resp = Response(js, status=200, mimetype='application/json')
    return resp


if __name__ == '__main__':
    app.run()
