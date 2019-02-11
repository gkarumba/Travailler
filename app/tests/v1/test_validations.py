import json

from app.api.v1.models.users_models import UserModels
from app.tests.v1.test_base import BaseTest

class TestEndpoints(BaseTest):
    """
    Class for testing the books endpoints
    """
    def test_validate_email(self):
        """ 
        Method for testing the user registration
        """
        response = self.client.post('/api/v1/user/register',data=json.dumps(self.register_email),content_type='application/json')
        result = json.loads(response.data)
        # import pdb; pdb.set_trace()
        self.assertEqual(response.status_code, 400)
        self.assertIn(result['message'],'Invalid Email')
    
    def test_validate_username(self):
        """ 
        Method for testing the user registration
        """
        response = self.client.post('/api/v1/user/register',data=json.dumps(self.register_username),content_type='application/json')
        result = json.loads(response.data)
        # import pdb; pdb.set_trace()
        self.assertEqual(response.status_code, 400)
        self.assertIn(result['message'],'Invalid username')
    
    def test_validate_age(self):
        """ 
        Method for testing the user registration
        """
        response = self.client.post('/api/v1/user/register',data=json.dumps(self.register_age),content_type='application/json')
        result = json.loads(response.data)
        # import pdb; pdb.set_trace()
        self.assertEqual(response.status_code, 400)
        self.assertIn(result['message'],'Invalid age')
    
    def test_validate_education(self):
        """ 
        Method for testing the user registration
        """
        response = self.client.post('/api/v1/user/register',data=json.dumps(self.register_education),content_type='application/json')
        result = json.loads(response.data)
        # import pdb; pdb.set_trace()
        self.assertEqual(response.status_code, 400)
        self.assertIn(result['message'],'Invalid education')
    
    def test_validate_password(self):
        """ 
        Method for testing the user registration
        """
        response = self.client.post('/api/v1/user/register',data=json.dumps(self.register_password),content_type='application/json')
        result = json.loads(response.data)
        # import pdb; pdb.set_trace()
        self.assertEqual(response.status_code, 400)
        self.assertIn(result['message'],'Invalid Password,atleast 8 characters')

    def test_validate_NationalID(self):
        """ 
        Method for testing the user registration
        """
        response = self.client.post('/api/v1/user/register',data=json.dumps(self.register_NationalID),content_type='application/json')
        result = json.loads(response.data)
        # import pdb; pdb.set_trace()
        self.assertEqual(response.status_code, 400)
        self.assertIn(result['message'],'Invalid nationaId')
    
    def test_validate_occupation(self):
        """ 
        Method for testing the user registration
        """
        response = self.client.post('/api/v1/user/register',data=json.dumps(self.register_occupation),content_type='application/json')
        result = json.loads(response.data)
        # import pdb; pdb.set_trace()
        self.assertEqual(response.status_code, 400)
        self.assertIn(result['message'],'Invalid occupation')


    