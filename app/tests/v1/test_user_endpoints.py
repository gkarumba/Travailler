import unittest
import json

from app.api.v1.models.users_models import UserModels
from app.tests.v1.test_base import BaseTest

class TestEndpoints(BaseTest):
    """
    Class for testing the books endpoints
    """
    def test_register(self):
        """ 
        Method for testing the user registration
        """
        response = self.client.post('/api/v1/user/register',data=json.dumps(self.register),content_type='application/json')
        result = json.loads(response.data)
        # import pdb; pdb.set_trace()
        self.assertEqual(response.status_code, 201)
        self.assertIn(result['data'][0]['message'],'user succesfully created')

    def test_login(self):
        """ 
        Method for testing the user login 
        """
        self.client.post('/api/v1/user/register',data=json.dumps(self.register_login),content_type='application/json')
        response = self.client.post('/api/v1/user/login',data=json.dumps(self.login),content_type='application/json')
        result = json.loads(response.data)
        # import pdb; pdb.set_trace()
        self.assertEqual(response.status_code, 200)
        self.assertIn(result['data'][0]['message'],'user succesfully logged in')


if __name__ == "__main__":
    unittest.main()