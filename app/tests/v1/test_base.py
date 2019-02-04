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
            "NationalID": 12345670
        }

        self.register_login = {
            "username": "string",
            "email": "string@email.com",
            "password": "string98",
            "age": 20,
            "location": "string",
            "occupation": "Employed",
            "education": "Degree",
            "NationalID": 12345679
        }
        self.register_email = {
            "username": "string",
            "email": "stringemail.com",
            "password": "string98",
            "age": 20,
            "location": "string",
            "occupation": "Employed",
            "education": "Degree",
            "NationalID": 12345679
        }
        self.register_username = {
            "username": "123456",
            "email": "string@email.com",
            "password": "string98",
            "age": 20,
            "location": "string",
            "occupation": "Employed",
            "education": "Degree",
            "NationalID": 12345679
        }
        self.register_age = {
            "username": "string",
            "email": "string@email.com",
            "password": "string98",
            "age": 9,
            "location": "string",
            "occupation": "Employed",
            "education": "Degree",
            "NationalID": 12345679
        }
        self.register_education = {
            "username": "string",
            "email": "string@email.com",
            "password": "string98",
            "age": 20,
            "location": "string",
            "occupation": "Employed",
            "education": "Degre",
            "NationalID": 12345679
        }
        self.register_password = {
            "username": "string",
            "email": "string@email.com",
            "password": "strin98",
            "age": 20,
            "location": "string",
            "occupation": "Employed",
            "education": "Degree",
            "NationalID": 12345679
        }
        self.register_NationalID = {
            "username": "string",
            "email": "string@email.com",
            "password": "string98",
            "age": 20,
            "location": "string",
            "occupation": "Employed",
            "education": "Degree",
            "NationalID": 1234567
        }
        self.register_occupation = {
            "username": "string",
            "email": "string@email.com",
            "password": "string98",
            "age": 20,
            "location": "string",
            "occupation": "Employe",
            "education": "Degree",
            "NationalID": 1234567
        }
        
        self.login = {
            "username": "string",
            "password": "string98"
        }

        self.post_data = {
            "title":"JrElectEng",
            "category":"Engineer",
            "responsibility":"sweep",
            "company":"Dasani",
            "location":"sembakasi",
            "salary":"10000"
        }

        self.post_data2 = {
            "title":"Medofficer",
            "category":"Medicine",
            "responsibility":"sweep",
            "company":"Dasani",
            "location":"sembakasi",
            "salary":"10000"
        }