import unittest
import json

from app.api.users.v2.models import UserModel
from app.tests.v2.test_base import BaseTest

class TestEndpoints(BaseTest):
    """
    Class for testing the books endpoints
    """
    def test_register(self):
        """ 
        Method for testing the user registration
        """
        response = self.client.post('/api/v2/user/register',data=json.dumps(self.register),content_type='application/json')
        result = json.loads(response.data)
        # import pdb; pdb.set_trace()
        self.assertEqual(response.status_code, 201)
        self.assertIn(result['data'][0]['message'],'user succesfully created')

if __name__ == '__main__':
    unittest.main()