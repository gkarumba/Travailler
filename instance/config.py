"""
Configurations for the application
"""
import os

class Config:
    """
    Parent Configuration class
    """
    DEBUG = True
    CSRF_ENABLED = True

class DevelopmentConfig(Config):
    """
    Development stage configurations
    """
    DEBUG = True
    DB_URL = os.getenv('DATABASE_URL')

class TestingConfig(Config):
    """
    Testing stage configurations
    """
    DEBUG = True
    TESTING =  True
    DB_URL = os.getenv('TEST_DB_URL')
    
class ProductionConfig(Config):
    """
    Production stage configurations
    """
    DEBUG = False

config_by_name = dict(
    dev=DevelopmentConfig,
    testing=TestingConfig,
    production=ProductionConfig
)
