"""User views contains Signup and login Resources"""
from app.api.v2.models.parcels_model import ParcelModel
from app.api.v2.models.users_model import UserModel
from flask import Flask, request, make_response, json, jsonify
from flask_restful import Resource
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from validators.validators import Validators

db = ParcelModel()
userobj = UserModel()
validate = Validators()


class ParcelResource(Resource):
    """Resource for user registration."""

    @jwt_required
    def post(self):
        """Method for posting user data"""
        request_data = request.get_json()
        if not request_data:
            return {"message": "Please provide a json data"}, 400
        if not all(key in request_data for key in ["pickup_location", "destination", "weight", "quantity", "recipient_name", "recepient_phone", "package_description"]):
            return {"message": "Some fields are missing"}, 400
        print(request_data)
        sender_Id = get_jwt_identity()
        pickup_location = request_data["pickup_location"]
        destination = request_data["destination"]
        weight = request_data["weight"]
        quantity = request_data["quantity"]
        recipient_name = request_data["recipient_name"]
        recepient_phone = request_data["recepient_phone"]
        package_description = request_data["package_description"]
        status = "active"
        current_location = pickup_location
        price = "Kshs." + str(float(weight) * 100)

        if pickup_location == "" or destination == "" or package_description == "":
            return {'message': "Please fill all the filds"}, 400

        if isinstance(weight, str) or isinstance(quantity, str) or isinstance(recepient_phone, str):
            return {'message': "Make sure weight, quantity or recipient are numbers"}, 400

        if weight <= 0 or quantity <= 0 or recepient_phone <= 0:
            return {'message': "Make sure weight, quantity or phone are 0 or negative"}, 400

        if not validate.valid_name(recipient_name):
            return {'message': "recipient name cant be empty and should only contain letters "}, 400

        check_role = validate.check_role(sender_Id)
        role = "user"

        if check_role == role:

            db.add_parcel(sender_Id, pickup_location, destination, weight, quantity, recipient_name,
                          recepient_phone, package_description, status, current_location, price)
            return {"message": "Parcel successfully created"}, 201

        return {"message": "Orders cannot be created on admin account"}, 400

    @jwt_required
    def put(self, parcel_id):
        """ changes the destination of an order"""
        sender_Id = get_jwt_identity()
        request_data = request.get_json()
        if not request_data:
            return {"message": "Please provide a json data"}, 400
        destination = request_data["destination"]

        if destination == "":
            return {"message": "please put the destination"}
        parcel = db.get_specific_parcel(parcel_id)
        if not parcel:
            return {"Message": "Parcel not found"}, 404

        status = parcel["status"]
        if status == 'cancelled' or status == 'delivered':
            return {"message": "You can't change the destination of a cancelled or delivered order"}
        check_role = validate.check_role(sender_Id)
        role = "user"
        if check_role == role:
            db.update_destination(destination, parcel_id)
            return {"message": "updated destination"}
        return {"message": "An admin cant update the destination"}, 400


class ParcelSpecific(Resource):
    """ class for specific parcel """

    @jwt_required
    def get(self, parcel_id):
        """getting a parcel delivery record by the ID"""
        parcel = db.get_specific_parcel(parcel_id)
        if parcel:
            return {'parcel order': parcel}, 200
        return {'message': "parcel order not found"}, 404

    @jwt_required
    def put(self, parcel_id):
        """ changes the status of an order"""
        sender_Id = get_jwt_identity()
        request_data = request.get_json()
        if not request_data:
            return {"message": "Please provide a json data"}, 400
        status = request_data["status"]

        if status == "":
            return {"message": "please put the status"}
        parcel = db.get_specific_parcel(parcel_id)
        if not parcel:
            return {"Message": "Parcel not found"}, 404

        check_role = validate.check_role(sender_Id)
        role = "admin"
        if check_role == role:
            db.update_status(status, parcel_id)
            return {"message": "updated destination"}
        return {"message": "An user cant update the status"}, 400
