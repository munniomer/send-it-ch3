import os
import psycopg2
"""import the list of tables"""
from .db_tables import queries

db_url = os.getenv('DATABASE_URL')


def connect_to_db(db_url):
    """making a connection to the db"""

    return psycopg2.connect(db_url)


def initialize_db():
    try:
        """starting the database"""
        connection = connect_to_db(db_url)

        """activate cursor"""
        cursor = connection.cursor()  # creating the cursor
        for query in queries:

            cursor.execute(query)

        connection.commit()  # saves changes to the DB
        connection.close()
        cursor.close()

    except (Exception, psycopg2.Error) as error:
        # returns error when the connectin fails
        print("Not unable to connect to the database", error)
