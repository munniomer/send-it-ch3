"""This module holds the database connection settings"""
import os
import psycopg2
from config import app_config
from .db_tables import queries, tablequeries

env = os.getenv("FLASK_ENV")
db_url = app_config[env].DATABASE_URL


def connect_to_db():
    """making a connection to the db"""
    try:
        print('Connecting to the PostgreSQL database...')
        return psycopg2.connect("dbname='test_send' host='localhost' port='5432' user='postgres' password=''")

    except (Exception, psycopg2.Error) as error:
        print("Not unable to connect to the database", error)


def create_tables():
    """creating tables for the database"""
    try:
        conn = connect_to_db()
        cursor = conn.cursor()
        for query in queries:
            cursor.execute(query)
        conn.commit()
    except (Exception, psycopg2.Error) as error:
        print("Not unable to create tables", error)
 


def destroy_tables():
    """Destroying tables for the test database"""
    try:
        conn = connect_to_db()
        cursor = conn.cursor()
        for table in tablequeries:
            cursor.execute(table)
        conn.commit()
    except (Exception, psycopg2.Error) as error:
        print("Not unable to destroy tables", error)

        
