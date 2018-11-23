"""User views contains Signup and login Resources"""
from app.api.v2.models.users_model import UserModel
from flask import Flask, request, make_response, json, jsonify
from flask_restful import Resource
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
from validators.validators import Validators

db = UserModel()
validators = Validators()


class SignupResource(Resource):
    """Resource for user registration."""

    def post(self):
        """Method for posting user data"""

        request_data = request.get_json()

        if not request_data:
            return {"message": "Please provide a json data"}, 400
        if not all(key in request_data for key in ["first_name", "last_name", "username", "email", "password", "confirm_password", "city", "role"]):
            return {"message": "Some fields are missing"}, 400

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
            return {'message': "PLease check if  city or username is empty"}, 400

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


class LoginResource(Resource):
    """Resource for user login """

    def post(self):
        """method for login users"""
        request_data = request.get_json()

        if not request_data:
            return {"message": "Please provide a correct json data"}, 400

        if not all(key in request_data for key in ["email", "password"]):
            return {"message": "Please provide your email and password"}, 400

        print(request_data)
        email = request_data["email"]
        password = request_data["password"]

        if not isinstance(email, str):
            return{"Message": "email cant be a number"},400

        if not validators.check_email(email):
            return {"message": "That email does not exist. Please register first"}, 404

        result = validators.check_email(email)
        userpass = result[6]
        userid = result[0]

        if check_password_hash(userpass, password):
            token = create_access_token(userid)
            return {"message": "Successfully loged in",
                    "token": token},200
        return {"message": "Password is incorrect"}, 400
