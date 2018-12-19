from lms.app import db
from lms.forms import AdminForm
from lms.utils import init_full_user, blank_resp
from werkzeug.datastructures import MultiDict


def register_admin(event):
    answer = blank_resp()

    form = AdminForm(data=event)
    try:

        if form.validate():
            user = init_full_user(form)
            db.session.add(user)
            db.session.commit()
        else:
            raise Exception(str(form.errors.items()))

    except Exception as e:
        answer['status'] = 'error'
        answer['error_message'] = str(e)

    return answer


# example
d = MultiDict({
    'status': 'admin',
    'username': 'admin1',
    'email': 'admin@mail.ru',
    'password': 'qwerty',
    'name': 'Admin',
    'surname': 'Adminov',
    'second_name': 'Adminovich'
})

answer = register_admin(d)

print(str(answer))
