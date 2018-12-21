from flask import Flask
import unittest
from flask import jsonify
import json
from flask_sqlalchemy import SQLAlchemy
from lms.app import app
from lms.Domain.Users import User
from lms.Domain.Courses import Course
from lms.Domain.Students import Student, Group
from lms.Domain.Teachers import Teacher
from flask_login import current_user

db = SQLAlchemy(app)


class appDBTests(unittest.TestCase):

    def setUp(self):
        """
        Creates a new database for the unit test to use
        """
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'

        db.init_app(app)

    def tearDown(self):
        """
        Ensures that the database is emptied for next unit test
        """
        db.init_app(app)
        with app.app_context():
            db.drop_all()

    def test_create_course(self):
        """Ensure a new course can not be added to the database without login."""
        with app.test_client() as client:
            response = client.post(
                '/create_course',
                data=json.dumps(dict(
                    name='test course',
                    description='test course description'
                )),
                content_type='application/json',

            )
            assert response.status_code == 401
