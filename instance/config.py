"""
Configurations for the application
"""
import os

class Config:
    """
    Parent Configuration class
    """
    DEBUG = False
    CSRF_ENABLED = True

class DevelopmentConfig(Config):
    """
    Development stage configurations
    """
    DEBUG = True

class TestingConfig(Config):
    """
    Testing stage configurations
    """
    DEBUG = True
    TESTING =  True
    
class ProductionConfig(Config):
    """
    Production stage configurations
    """
    DEBUG = False

config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)
