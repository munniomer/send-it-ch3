import os


class Config():
    """Parent configuration class."""
    DEBUG = False
    TESTING = False
    CSRF_ENABLE = True
    SECRET_KEY = os.getenv('munira')


class Development(Config):
    """Configurations for Development."""
    DEBUG = True
    TESTING = True


class Production(Config):
    """Configurations for Production."""
    DEBUG = False
    TESTING = False


class Testing(Config):
    """Configurations for Testing, with a separate test database."""
    DEBUG = True
    TESTING = True


app_config = {
    "development": Development,
    "testing": Testing,
    "production": Production
}
