"""User views contains Signup and login Resources"""
from app.api.v2.models.users_model import UserModel
from flask import Flask, request, make_response, json, jsonify
from flask_restful import Resource
from werkzeug.security import generate_password_hash, check_password_hash
from validators.validators import Validators

db = UserModel()
validators = Validators()


class SignupResource(Resource):
    """Resource for user registration."""

    def post(self):
        """Method for posting user data"""

        request_data = request.get_json()

        first_name = request_data["first_name"]
        last_name = request_data["last_name"]
        username = request_data["username"]
        email = request_data["email"]
        phone = request_data["phone"]
        password = request_data["password"]
        confirm_password = request_data["confirm_password"]
        city = request_data["city"]
        role = request_data["role"]

        if not validators.valid_email(email):
            return {'message': "Please enter a valid email "}, 400

        if not validators.valid_name(first_name) or not validators.valid_name(last_name) or not validators.valid_name(role):
            return {'message': "PLease check if your first_name, last_name  or role is empty or contains numbers"}, 400

        if not validators.valid_user_field(city) or not validators.valid_user_field(username):
            return {'message': "PLease check if  city or username is empty or contains numbers"}, 400

        if not isinstance(phone, int):
            return {'message': "Please enter a valid phone number "}, 400

        if confirm_password != password:
            return {"message": "confirm password does not match password"}, 400

        if validators.check_email(email):
            return {"message": "That email exist. Please Choose another one"}, 400

        if validators.check_username(username):
            return {"message": "That username exist.Please Choose another one"}, 400

        if validators.check_phone(phone):
            return {"message": "That phone exist.Please Choose another one"}, 400

        hashpassword = generate_password_hash(password)

        if not validators.valid_password(password) or not validators.valid_password(confirm_password):
            return {'message': "Please check if your password or confirm password are empty or less than 3"}, 400

        if confirm_password != password:
            return {"message": "confirm password does not match password"}, 400

        db.add_user(first_name, last_name, username, email, phone,
                    hashpassword, city, role)
                    
        return {"message": "User successfully created"}, 201
