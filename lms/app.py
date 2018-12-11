from flask import Flask
from .config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from .Domain import User, Course, Student, Group, Teacher


APP = Flask(__name__)
APP.config.from_object(Config)
DB = SQLAlchemy(APP)
MIGRATE = Migrate(APP, DB)


@APP.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    APP.run()
