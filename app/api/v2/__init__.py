from flask import Flask, Blueprint
from flask_restful import Api, Resource 
from app.api.v2.views.users_view import SignupResource,LoginResource
from app.api.v2.views.parcels_view import ParcelResource,ParcelSpecific

v2 = Blueprint('apiv1', __name__, url_prefix='/api/v2')
app = Api(v2)  

# Users
app.add_resource(SignupResource, '/auth/signup')
app.add_resource(LoginResource, '/auth/login')

#parcels
app.add_resource(ParcelResource, '/parcels', '/parcels/<int:parcel_id>/destination')
app.add_resource(ParcelSpecific, '/parcels/<int:parcel_id>', '/parcels/<int:parcel_id>/status')
