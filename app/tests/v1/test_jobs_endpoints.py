import unittest
import json

from app.api.v1.models.jobs_models import JobsModel
from app.tests.v1.test_base import BaseTest

class TestEndpoints(BaseTest):
    """
    Class for testing the jobs endpoints
    """
    def test_post(self):
        """ 
        Method for testing the post job endpoint
        """
        response =  self.client.post('api/v1/jobs',\
                                      data=json.dumps(self.post_data),\
                                      content_type='application/json')
        result = json.loads(response.data)
        # import pdb; pdb.set_trace()
        self.assertTrue(response.status_code, 201)
        self.assertIn(result['data'][0]['message'],'job succesfully added')

    def test_get(self):
        """
        Method for testing the get job endpoint
        """
        self.client.post('api/v1/jobs',\
                          data=json.dumps(self.post_data2),\
                          content_type='application/json')
        response = self.client.get('api/v1/jobs',\
                         data=json.dumps(self.post_data2),\
                        content_type='application/json')
        result = json.loads(response.data)
        # import pdb; pdb.set_trace()
        self.assertTrue(response.status_code, 200)
        self.assertIn(result['data'][0]['message'], 'jobs available')

    def test_get_one(self):
        """
        Method for testing the get job by category endpoint
        """
        self.client.post('api/v1/jobs',\
                          data=json.dumps(self.post_data2),\
                          content_type='application/json')
        response = self.client.get('api/v1/jobs/1',\
                         data=json.dumps(self.post_data2),\
                        content_type='application/json')
        result = json.loads(response.data)
        # import pdb; pdb.set_trace()
        self.assertTrue(response.status_code, 200)
        self.assertIn(result['data'][0]['message'], 'jobs available')

    def test_edit_job(self):
        """
        Method to test the editing a job
        """
        self.client.post('api/v1/jobs',\
                          data=json.dumps(self.post_data2),\
                          content_type='application/json')
        response = self.client.put('api/v1/jobs/edit/1',\
                         data=json.dumps(self.edit_data),\
                        content_type='application/json')
        result = json.loads(response.data)
        # import pdb; pdb.set_trace()
        self.assertTrue(response.status_code, 200)
        self.assertIn(result['data'][0]['message'], 'job edited succesfully')

    def test_delete_job(self):
        """
        Method to test the deletng a job
        """
        self.client.post('api/v1/jobs',\
                          data=json.dumps(self.post_data2),\
                          content_type='application/json')
        response = self.client.delete('api/v1/jobs/delete/1',\
                         data=json.dumps(self.edit_data),\
                        content_type='application/json')
        result = json.loads(response.data)
        # import pdb; pdb.set_trace()
        self.assertTrue(response.status_code, 200)
        self.assertIn(result['data'][0]['message'], 'job deleted succesfully')


if __name__ == '__main__':
    unittest.main()