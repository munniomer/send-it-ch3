import unittest
from app import create_app
import json
from tests.basetest import BaseTest


class TestParcel(BaseTest):
    """User tests class"""

    def authorize(self):
        self.client.post(
        "/api/v2/auth/signup", json=self.new_user0, content_type='application/json')
        respon = self.client.post(
        "/api/v2/auth/login", json=self.new_user01, content_type='application/json')
        self.assertEqual(respon.status_code, 200)
        token = json.loads(respon.get_data(as_text=True))['token']
        header = {'Authorization': 'Bearer {}'.format(token)}
        return header


    def test_if_no_data(self):
        """Tests if no data is provided in user signup"""
        respon= self.client.post(
            "/api/v2/parcels",headers=self.authorize())
        self.assertEqual(respon.status_code, 400)
        self.assertIn('Please provide a json data',
                      str(respon.data))
    
    def test_if_fields_missing(self):
        """Tests if some fields are missing in user signup"""
        respon=self.client.post(
            "/api/v2/parcels", json=self.new_parcel6, content_type='application/json', headers=self.authorize())
        self.assertEqual(respon.status_code, 400)
        self.assertIn('Some fields are missing',
                      str(respon.data))


    def test_parcel_creation(self):
        """tests if parcel can be created"""
        respon = self.client.post(
            "/api/v2/parcels", json=self.new_parcel, content_type='application/json', headers=self.authorize())
        self.assertIn(
            "Parcel successfully created", str(respon.data))

    def test_if_argument_has_invalid_data(self):
        """Tests if a invalid data is provided"""
        respon = self.client.post(
        "/api/v2/parcels", json=self.new_parcel3, content_type='application/json', headers=self.authorize())
        self.assertEqual(respon.status_code, 400)
        self.assertIn('Make sure weight, quantity or recipient are numbers',
                    str(respon.data))

    def test_if_argument_is_provided(self):
        """Tests if there is empty fields"""
        respon = self.client.post(
            "/api/v2/parcels", json=self.new_parcel4, content_type='application/json',headers=self.authorize())
        self.assertEqual(respon.status_code, 400)
        self.assertIn('Please fill all the filds',
                      str(respon.data))

    def test_recipient_name(self):
        """Tests if there is empty fields"""
        respon = self.client.post(
            "/api/v2/parcels", json=self.new_parcel5, content_type='application/json',headers=self.authorize())
        self.assertEqual(respon.status_code, 400)
        self.assertIn('recipient name cant be empty and should only contain letters',
                      str(respon.data))

    def test_if_arguemnt_has_negative_values(self):
        """Tests if a negative value is provided"""
        respon = self.client.post(
            "/api/v2/parcels", json=self.new_parcel2, content_type='application/json',headers=self.authorize())
        self.assertEqual(respon.status_code, 400)
        self.assertIn('Make sure weight, quantity or phone are 0 or negative',
                      str(respon.data))







 