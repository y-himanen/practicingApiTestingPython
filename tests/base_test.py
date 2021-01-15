"""
BaseTest

This class should be the parent class to each non-unit test.
It allows for instantiation of the database dynamically
and makes sure that it is a new, blank database each time.
"""

from unittest import TestCase
from app import app
from db import db


class BaseTest(TestCase):
    @classmethod
    def setUpClass(cls):
        # Runs once for each test class, so can put in things that only need to be done once
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'
        # The following two configurations need to be included to run the whole test suite without
        # Flask complaining that the first request was already made before starting up the app.
        app.config['DEBUG'] = False
        # Needs to be set manually, as usually set automatically by debug when true.
        app.config['PROPAGATE_EXCEPTIONS'] = True
        with app.app_context():
            db.init_app(app)

    def setUp(self):
        # Runs once for every test method
        # Make sure database exists
        # Remember that sqlite doesn't enforce foreign key checking
        with app.app_context():
            db.create_all()
        # Get a test client
        self.app = app.test_client
        self.app_context = app.app_context

    def tearDown(self):
        # Database is blank
        with app.app_context():
            db.session.remove()
            db.drop_all()
