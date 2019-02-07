import unittest
from app import create_app

class BaseTest(unittest.TestCase):
    """
    Class for setting up the tests
    """
    def setUp(self):
        """
        Method for setting up the tests
        """
        self.app_test = create_app()
        self.client = self.app_test.test_client()
        self.app_test.testing = True

        self.register = {
            "username": "string",
            "email": "string@email.com",
            "password": "string98",
            "age": 20,
            "location": "string",
            "occupation": "Employed",
            "education": "Degree",
            "nationalID": 12345670
        }
