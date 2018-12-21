from flask import Flask
import unittest
from flask import jsonify
import json
from flask_sqlalchemy import SQLAlchemy
from lms.app import app, db
from lms.Domain.Users import User
from lms.Domain.Courses import Course
from lms.Domain.Students import Student, Group
from lms.Domain.Teachers import Teacher
from lms.utils import generate_validation_code
import os

app.config['DEBUG'] = True
app.config['TESTING'] = True

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'test.db')


class appDBTests(unittest.TestCase):

    def setUp(self):
        """
        Creates a new database for the unit test to use
        """
        with app.app_context():
            db.create_all()
            user = User(
                name="test",
                surname="test",
                second_name="test",
                status="student",
                registration_uid="A1"
            )
            db.session.add(user)
            db.session.commit()

    def tearDown(self):
        """
        Ensures that the database is emptied for next unit test
        """
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

    def test_user_register(self):
        with app.test_client() as client:
            response = client.post(
                '/register',
                data='validation_code="A1"&'
                     'username="test"&'
                     'email="a@a.ru"&'
                     'password="a"',
                content_type='application/x-www-form-urlencoded',
            )
            assert response.status_code == 400
