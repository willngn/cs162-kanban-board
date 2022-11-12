# i learned mostly from these sources: https://blog.miguelgrinberg.com/post/how-to-write-unit-tests-in-python-part-3-web-applications
# https://www.patricksoftwareblog.com/unit-testing-a-flask-application/
# https://greyli.com/flask-tutorial-chapter-9-test/

from src import app, db
from flask import current_app
import unittest

class generalTesting(unittest.TestCase):
    def setUp(self):
        """Before every test case"""
        app.config.update(TESTING=True)
        self.context = app.test_request_context()
        self.context.push()
        self.app = app.test_client()
        # make sure clean db
        db.drop_all()
        db.create_all()
        db.session.commit()

    def tearDown(self):
        """After every test case"""
        pass

    def testApp(self):
        """App exists! and in testing mode!"""
        assert current_app is not None
        assert current_app.config['TESTING'] == True
if __name__ == '__main__':
    unittest.main()
