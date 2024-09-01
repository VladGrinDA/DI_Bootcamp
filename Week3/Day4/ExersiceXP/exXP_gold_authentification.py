# import sys
# import os

# print('cwd', os.getcwd())

# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))
# print(*sys.path, sep='\n')

# from credentials import *
import psycopg2

USER = "postgres" 
PASSWORD = "vlad312312" 
HOST = "localhost"
PORT = "5432" # or 5433

DB_NAME = 'public'

class DB:
    def __init__(self, host, db_name, password, username, port='5432') -> None:
        self.connection = psycopg2.connect(
            dbname = db_name,
            user = username,
            password = password,
            host = host,
            port = port
        )
    
    def __del__(self) -> None:
        self.connection.close()

    @property
    def conn(self):
        return self.connection
    
    def cursor(self):
        return self.connection.cursor()

    def execute(self, query):
        with self.connection.cursor() as cursor:
            cursor.execute(query)
            self.connection.commit()
            return cursor
    
    