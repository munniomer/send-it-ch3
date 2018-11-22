import os


class Config():
    """Parent configuration class."""
    DEBUG = False
    TESTING = False
    CSRF_ENABLE = True
    JWT_SECRET_KEY = os.getenv("SECRET_KEY")
    DATABASE_URL = os.getenv("DATABASE_URL")


class Development(Config):
    """Configurations for Development."""
    DEBUG = True
    TESTING = True
    DATABASE_URL = os.getenv("DATABASE_send_URL")


class Production(Config):
    """Configurations for Production."""
    DEBUG = False
    TESTING = False


class Testing(Config):
    """Configurations for Testing, with a separate test database."""
    DEBUG = True
    TESTING = True
    DATABASE_URL = os.getenv("DATABASE_TEST_URL")


app_config = {
    "development": Development,
    "testing": Testing,
    "production": Production
}