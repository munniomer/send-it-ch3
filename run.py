import os
from app import create_app
from app.database.db_connection import create_tables, destroy_tables

config_name = os.getenv("FLASK_ENV")
app = create_app(config_name)

    create_tables()

if __name__ == "__main__":
    app.run(debug=True)
