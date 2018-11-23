import re
from app.database.db_connection import connect_to_db

class Validators():
    def check_email(self,email):
        """checks if email exists"""
        con = connect_to_db()
        cursor = con.cursor()
        cursor.execute ("select * from users where email = %s",([email]))
        return cursor.fetchone()

    def check_role(self,sender_Id):
        """checks if user role"""
        con = connect_to_db()
        cursor = con.cursor()
        cursor.execute ("select role from users where user_id = %s",([sender_Id]))
        return cursor.fetchone()[0]

    def check_username(self,username):
        """checks if username exists"""
        con = connect_to_db()
        cursor = con.cursor()
        cursor.execute ("select * from users where username = %s",([username]))
        return cursor.fetchone()

    def check_phone(self,phone):
        """checks if phone exists"""
        con = connect_to_db()
        cursor = con.cursor()
        cursor.execute ("select * from users where phone = %s",([phone]))
        return cursor.fetchone()

    def valid_name(self, name):
        """validate first name and last name"""
        regex = "^[a-zA-Z]{1,}$"
        return re.match(regex, name)


    def valid_user_field(self, name):
        """validate user field"""
        regex = "^[a-zA-Z0-9]{2,}$"
        return re.match(regex, name)

    def valid_email(self, email):
        """ valid email """
        regex = "^[\w]+[\d]?@[\w]+\.[\w]+$"
        return re.match(regex, email)

    def valid_password(self, password):
        """ valid password """
        regex = "^[a-zA-Z0-9@_+-.]{3,}$"
        return re.match(regex, password)

       