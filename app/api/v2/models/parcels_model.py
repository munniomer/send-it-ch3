from app.database.db_connection import connect_to_db
from psycopg2.extras import RealDictCursor
import psycopg2
class ParcelModel(object):
    """Class Parcel models."""
    def __init__(self):
        """Initializes the parcel db"""
        self.db = connect_to_db()

    def add_parcel(self, sender_Id,pickup_location, destination, weight,
                   quantity, recipient_name, recipient_phone, package_description,status,current_location,price):
        """ Method for saving user to the dictionary """
        payload = {
            "sender_Id": sender_Id,
            "pickup_location": pickup_location,
            "destination":  destination,
            "weight":  str(weight) + "kg",
            "quantity": quantity,
            "recipient_name": recipient_name,
            "recepient_phone": recipient_phone,
            "package_description": package_description,
            "status": "active",
            "current_location": pickup_location,
            "price": "Kshs." + str(float(weight) * 100)
        }

        try:
            query = """INSERT INTO parcels(sender_Id,pickup_location, destination, weight,quantity, recipient_name, recepient_phone,package_description,status,current_location,price) VALUES (%(sender_Id)s,%(pickup_location)s, %(destination)s, %(weight)s, %(quantity)s, %(recipient_name)s,%(recepient_phone)s,%(package_description)s,%(status)s,%(current_location)s,%(price)s)"""
            cursor = self.db.cursor()
            cursor.execute(query, payload)
            self.db.commit()
        except (Exception, psycopg2.Error) as error:
            print(error)
            return {"message": "Not able to insert in parcels table"},400