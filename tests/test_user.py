import unittest
from app import create_app
import json
from tests.basetest import BaseTest


class TestUSer(BaseTest):
    """User tests class"""

    def test_user_registration(self):
        "tests if new user can register"
        respon = self.client.post("/api/v2/auth/signup", json=self.new_user, content_type='application/json')
        self.assertEqual(respon.status_code, 201)
        self.assertIn('User successfully created',
                      str(respon.data))

    def test_valid_name(self):
        """Tests if names and role are valid"""
        respon = self.client.post(
            "/api/v2/auth/signup", json=self.new_user1, content_type='application/json')
        self.assertEqual(respon.status_code, 400)
        self.assertIn('PLease check if your first_name, last_name  or role is empty or contains numbers',
                      str(respon.data))


    def test_valid_field(self):
        """Tests if username and city are valid"""
        respon = self.client.post(
            "/api/v2/auth/signup", json=self.new_user2, content_type='application/json')
        self.assertEqual(respon.status_code, 400)
        self.assertIn('PLease check if  city or username is empty',
                      str(respon.data))


    def test_if_email_valid(self):
        """Tests if email is valid"""
        respon = self.client.post(
          "/api/v2/auth/signup", json=self.new_user3, content_type='application/json')
        self.assertEqual(respon.status_code, 400)
        self.assertIn('Please enter a valid email',
                      str(respon.data))

    def test_if_phone_valid(self):
        """Tests if email is exists"""
        respon = self.client.post(
            "/api/v2/auth/signup", json=self.new_user4, content_type='application/json')
        self.assertEqual(respon.status_code, 400)
        self.assertIn('Please enter a valid phone number ',
                      str(respon.data))


    def test_if_password_valid(self):
        """Tests if passwords are empty or less than 3"""
        respon = self.client.post(
             "/api/v2/auth/signup", json=self.new_user5, content_type='application/json')
        self.assertEqual(respon.status_code, 400)
        self.assertIn('Please check if your password or confirm password are empty or less than 3',
                      str(respon.data))

    def test_if_password_match(self):
        """Tests if passwords match"""
        respon = self.client.post(
            "/api/v2/auth/signup", json=self.new_user6, content_type='application/json')
        self.assertEqual(respon.status_code, 400)
        self.assertIn('confirm password does not match password',
                      str(respon.data))

    
    def test_if_email_exist(self):
        """Tests if email is exists"""
        self.client.post(
            "/api/v2/auth/signup", json=self.new_user7, content_type='application/json')
        respon = self.client.post(
           "/api/v2/auth/signup", json=self.new_user7, content_type='application/json')
        self.assertEqual(respon.status_code, 400)
        self.assertIn('That email exist. Please Choose another one',
                      str(respon.data))


    def test_if_username_exist(self):
        """Tests if username is exists"""
        self.client.post(
            "/api/v2/auth/signup", json=self.new_user8, content_type='application/json')
        respon = self.client.post(
           "/api/v2/auth/signup", json=self.new_user9, content_type='application/json')
        self.assertEqual(respon.status_code, 400)
        self.assertIn('That username exist.Please Choose another one',
                      str(respon.data))
    
    def test_if_phone_exist(self):
        """Tests if username is exists"""
        self.client.post(
            "/api/v2/auth/signup", json=self.new_user10, content_type='application/json')
        respon = self.client.post(
           "/api/v2/auth/signup", json=self.new_user11, content_type='application/json')
        self.assertEqual(respon.status_code, 400)
        self.assertIn('That phone exist.Please Choose another one',
                      str(respon.data))
    
    def test_if_no_data(self):
        """Tests if no data is provided in user signup"""
        respon= self.client.post(
            "/api/v2/auth/signup")
        self.assertEqual(respon.status_code, 400)
        self.assertIn('Please provide a json data',
                      str(respon.data))
    
    def test_if_fields_missing(self):
        """Tests if some fields are missing in user signup"""
        respon=self.client.post(
            "/api/v2/auth/signup", json=self.new_user12, content_type='application/json')
        self.assertEqual(respon.status_code, 400)
        self.assertIn('Some fields are missing',
                      str(respon.data))

    def test_user_login(self):
        "tests if user can login"
        self.client.post(
            "/api/v2/auth/signup", json=self.new_user, content_type='application/json')
        respon=self.client.post(
            "/api/v2/auth/login", json=self.new_user14, content_type='application/json')

        self.assertEqual(respon.status_code, 200)
        self.assertIn('Successfully loged in',
                      str(respon.data))


    def test_valid_data(self):
        """Tests if no data is provided in user login"""
        respon= self.client.post(
            "/api/v2/auth/login")
        self.assertEqual(respon.status_code, 400)
        self.assertIn('Please provide a correct json data',
                      str(respon.data))
    

    def test_missing_field(self):
        """Tests if some fields are missing in user signup"""
        respon=self.client.post(
            "/api/v2/auth/login", json=self.new_user13, content_type='application/json')
        self.assertEqual(respon.status_code, 400)
        self.assertIn('Please provide your email and password',
                      str(respon.data))

    def test_valid_email(self):
        """Tests if email is valid in user login"""
        self.client.post(
            "/api/v2/auth/signup", json=self.new_user, content_type='application/json')
        respon = self.client.post(
          "/api/v2/auth/login", json=self.new_user15, content_type='application/json')
        self.assertEqual(respon.status_code, 400)
        self.assertIn('email cant be a number',
                      str(respon.data))

    def test_email_not_exist(self):
        """Tests if email does not exist in user login"""
        self.client.post(
            "/api/v2/auth/signup", json=self.new_user6, content_type='application/json')
        respon = self.client.post(
           "/api/v2/auth/login", json=self.new_user14, content_type='application/json')
        self.assertEqual(respon.status_code, 404)
        self.assertIn('"That email does not exist. Please register first"',
                      str(respon.data))

    def test_password__match(self):
        """Tests if passwords match in user login"""
        self.client.post(
            "/api/v2/auth/signup", json=self.new_user, content_type='application/json')
        respon = self.client.post(
            "/api/v2/auth/login", json=self.new_user16, content_type='application/json')
        self.assertEqual(respon.status_code, 400)
        self.assertIn('Password is incorrect',
                      str(respon.data))

    

        
    



