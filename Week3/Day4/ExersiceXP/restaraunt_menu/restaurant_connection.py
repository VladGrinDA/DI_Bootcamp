import psycopg2
from credentials import *

DB_NAME = 'restaurant'

try:
    restaurant_connection = psycopg2.connect(
        dbname = DB_NAME,
        user = USER,
        password = PASSWORD,
        host = HOST,
        port = PORT
    )
except Exception as e:
    print(f"Error: {e}")