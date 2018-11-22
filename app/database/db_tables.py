"""creating tables for the database"""
users_table  = ''' CREATE TABLE IF NOT EXISTS users (
                user_id serial PRIMARY KEY, 
                first_name VARCHAR (30) NOT NULL, 
                last_name VARCHAR (30) NOT NULL, 
                username VARCHAR (30) UNIQUE NOT NULL, 
                email varchar(30) UNIQUE NOT NULL,
                phone integer UNIQUE NOT NULL,
                password VARCHAR (200) NOT NULL,
                city VARCHAR (30) NOT NULL,
                role varchar(30) DEFAULT 'user'
            )
            '''

parcels_table = ''' CREATE TABLE IF NOT EXISTS parcels (
            parcel_id  serial PRIMARY KEY,
            sender_id integer  REFERENCES users (user_id) ,
            pickup_location varchar(30) NOT NULL,
            destination varchar(30) NOT NULL,
            weight varchar(30) NOT NULL,
            quantity integer NOT NULL,
            recipient_name varchar(30) NOT NULL,
            recepient_phone varchar(30) NOT NULL,
            package_description varchar(30) NOT NULL,
            status varchar(30) DEFAULT 'active',
            current_location varchar(30),
            price varchar(30)
            )
            '''
queries = [users_table, parcels_table]

"""Destroying tables for the test database"""
table_users = ''' DROP TABLE IF EXISTS users CASCADE '''
table_parcels = ''' DROP TABLE IF EXISTS parcels CASCADE '''
tablequeries = [table_users , table_parcels]


