from werkzeug.datastructures import MultiDict
from lms.app import db
from lms.forms import AdminForm
from lms.utils import init_full_user, blank_resp


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

    except Exception as exception:
        answer['status'] = 'error'
        answer['error_message'] = str(exception)

    return answer


# example
example = MultiDict({
    'status': 'admin',
    'username': 'admin',
    'email': 'admin@mail.ru',
    'password': 'qwerty',
    'name': 'Admin',
    'surname': 'Adminov',
    'second_name': 'Adminovich'
})

result = register_admin(example)

print(str(result))
