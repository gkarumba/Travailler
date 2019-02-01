import unittest
from flask import current_app

from app import create_app

class TestDevelopmentConfig(unittest.TestCase):
    """
    Class with the method to test the developmentconfig
    """
    def test_app_is_development(self):
        """
        Method to test the developmentconfig
        """
        app = create_app()
        app.config.from_object('instance.config.DevelopmentConfig')
    
        self.assertTrue(app.config['DEBUG'] is True)
        self.assertFalse(current_app is None)

class TestTestingConfig(unittest.TestCase):
    """
    Class with the method to test the testingconfig
    """
    def test_app_is_testing(self):
        """
        Method to test the testingconfig
        """
        app = create_app()
        app.config.from_object('instance.config.TestingConfig')
        
        self.assertTrue(app.config['DEBUG'])
        self.assertTrue(app.config['TESTING'])

class TestProductionConfig(unittest.TestCase):  
    """
    Class with the method to test the productionconfig
    """   
    def test_app_is_production(self):
        """
        Method to test the productionconfig
        """
        app = create_app()
        app.config.from_object('instance.config.ProductionConfig')

        self.assertTrue(app.config['DEBUG'] is False)

if __name__ == '__main__':
    unittest.main()
