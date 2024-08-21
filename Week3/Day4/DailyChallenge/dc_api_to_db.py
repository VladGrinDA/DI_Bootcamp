
# Instructions
# Using this REST Countries API, create the functionality which will write 10 random countries to your database.

# These are the attributes which you should populate your tables with: name, capital, flag, subregion, population.

from pprint import pprint
import requests
import psycopg2
from psycopg2.extras import NamedTupleCursor

from credentials import *

DB_NAME = 'public'

try:
    connection = psycopg2.connect(
        dbname = DB_NAME,
        user = USER,
        password = PASSWORD,
        host = HOST,
        port = PORT
    )
except Exception as e:
    print(f"Error: {e}")


countries_api = requests.get('https://restcountries.com/v3.1/all')
print(countries_api)

data = countries_api.json()
pprint(data[1])


with connection.cursor() as cursor:
    cursor.execute('drop table if exists countries')

    cursor.execute('''
    create table countries (
        country_id serial primary key,
        country_name varchar(100) not null,
        capital varchar(100),
        flag varchar(50),
        subregion varchar(255),
        population integer
    );
    ''')

    connection.commit()

from collections import defaultdict

def process_string(x):
    return "\'%s\'" % x.replace("\'", "\'\'") if x != 'NULL' else x

print(process_string(defaultdict(lambda: 'NULL', data[0])['not_a_key']))

with connection.cursor(cursor_factory=NamedTupleCursor ) as cursor:
    for i in range(10):
        item = defaultdict(lambda: 'NULL', data[i])
        print(i, item['name']['official'])
        country_name = process_string(item['name']['official'])
        capital = process_string(item['capital'][0]) if len(item['capital']) > 0 else 'NULL'
        flag = process_string(item['flag'])
        # subregion = item.get(['subregion'], 'NULL')
        subregion = process_string(item['subregion'])
        population = item['population']

        cursor.execute(f'''
        insert into countries (country_name, capital, flag, subregion, population)
        values ({country_name}, {capital}, {flag}, {subregion}, {population})
        returning *;
        ''')

        print(cursor.fetchone())

    connection.commit()