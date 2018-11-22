from app.database.db_connection import connect_to_db
from app.database.db_connection import connect_to_db
import psycopg2


class UserModel(object):

    """Class user models."""

    def __init__(self):
        self.db = connect_to_db()

    def add_user(self, first_name, last_name, username, email, phone, password, city, role):
        """ Method for saving user to the dictionary """
        payload = {
            "first_name": first_name,
            "last_name": last_name,
            "username": username,
            "email":  email,
            "phone":  phone,
            "password": password,
            "city": city,
            "role": role
        }
        try:
            query = """INSERT INTO USERS(first_name, last_name, username, email, phone, password,city,role) VALUES (%(first_name)s, %(last_name)s, %(username)s, %(email)s, %(phone)s,%(password)s,%(city)s, %(role)s) """
            cursor = self.db.cursor()
            cursor.execute(query, payload)
            self.db.commit()
              
            return {"message": "User successfullt created"},201
        except (Exception, psycopg2.Error) as error:
            print(error)
            return {"message": "Not able to insert in users table"},400
