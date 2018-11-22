import unittest
from app import create_app
import json
from app.database.db_connection import destroy_tables
import os


class BaseTest(unittest.TestCase):
    """This is the test client"""

    def setUp(self):
        """Initialize app and define test variables"""
        os.environ["FLASK_ENV"] = "testing"

        self.app = create_app("testing")
        self.app.testing = True
        self.client = self.app.test_client()
        
        self.new_user ={
            "first_name": "Abdi",
            "last_name": "Farah",
            "username": "Abdalla",
            "email": "Abdi@gmail.com",
            "phone":  76367888,
            "password": "Abdi",
            "confirm_password": "Abdi",
            "city": "Kisumu",
            "role": "user"
    }

        self.new_user1 ={
        "first_name": "",
        "last_name": " ",
        "username": "Abdalla",
        "email": "Abdi@gmail.com",
        "phone":  76367888,
        "password": "Abdi",
        "confirm_password": "Abdi",
        "city": "Kisumu",
        "role": 888
}

        self.new_user2={
            "first_name": "Abdi",
            "last_name": "Farah",
            "username": " ",
            "email": "Abdi@gmail.com",
            "phone":  76367888,
            "password": "Abdi",
            "confirm_password": "Abdi",
            "city": "",
            "role": "user"
    }


        self.new_user3={
            "first_name": "Abdi",
            "last_name": "Farah",
            "username": " ",
            "email": "###gmail.com",
            "phone":  76367888,
            "password": "Abdi",
            "confirm_password": "Abdi",
            "city": "",
            "role": "user"
    }


        self.new_user4={
            "first_name": "Abdi",
            "last_name": "Farah",
            "username": "Muni",
            "email": "munira@gmail.com",
            "phone":  "",
            "password": "Abdi",
            "confirm_password": "Abdi",
            "city": "Muni",
            "role": "user"
    }


        self.new_user5={
            "first_name": "Abdi",
            "last_name": "Farah",
            "username": "Muni",
            "email": "munira@gmail.com",
            "phone":  677788,
            "password": " ",
            "confirm_password": " ",
            "city": "Muni",
            "role": "user"
    }


        self.new_user6={
            "first_name": "Abdi",
            "last_name": "Farah",
            "username": "Muni",
            "email": "munira@gmail.com",
            "phone":  677788,
            "password": "ab",
            "confirm_password": "cd",
            "city": "Muni",
            "role": "user"
    }

        self.new_user7 ={
            "first_name": "Abdi",
            "last_name": "Farah",
            "username": "Abda8lla",
            "email": "Asha@gmail.com",
            "phone":  763867888,
            "password": "Abdi",
            "confirm_password": "Abdi",
            "city": "Kisumu",
            "role": "user"
    }


        self.new_user8 ={
            "first_name": "Abdi",
            "last_name": "Farah",
            "username": "Hey",
            "email": "Ash9@gmail.com",
            "phone":  763678288,
            "password": "Abdi",
            "confirm_password": "Abdi",
            "city": "Kisumu",
            "role": "user"
    }

        self.new_user9 ={
            "first_name": "Abdi",
            "last_name": "Farah",
            "username": "Hey",
            "email": "Ashaa9@gmail.com",
            "phone":  768367888,
            "password": "Abdi",
            "confirm_password": "Abdi",
            "city": "Kisumu",
            "role": "user"
    }


        self.new_user10 ={
            "first_name": "Abdi",
            "last_name": "Farah",
            "username": "Heyo",
            "email": "Ashaa9@gmail.com",
            "phone":  768367888,
            "password": "Abdi",
            "confirm_password": "Abdi",
            "city": "Kisumu",
            "role": "user"
    }
        
        self.new_user11 ={
            "first_name": "Abdi",
            "last_name": "Farah",
            "username": "Hey",
            "email": "Ashaas9@gmail.com",
            "phone":  768367888,
            "password": "Abdi",
            "confirm_password": "Abdi",
            "city": "Kisumu",
            "role": "user"
    }




    def tearDown(self):
        destroy_tables()

if __name__ == '__main__':
    unittest.main(verbosity=2)