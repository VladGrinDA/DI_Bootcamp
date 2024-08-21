# Create a new database and a new table in pgAdmin (or in psql). The table is named Menu_Items and contains the columns

# item_id : SERIAL PRIMARY KEY
# item_name : VARCHAR(30) NOT NULL
# item_price : SMALLINT DEFAULT 0

# In the file menu_item.py, create a new class called MenuItem, the attributes should be the name and price of each item.

# Create several methods (save, delete, update) these methods will allow a user to save, delete and update items 
# from the Menu_Items table. The update method can update the name as well as the price of an item.

from restaurant_connection import restaurant_connection
from psycopg2.extras import NamedTupleCursor

class MenuItem:
    _table_name = 'menu_items'
    _connection = restaurant_connection
    # _cursor = restaurant_connection.cursor(cursor_factory=NamedTupleCursor)

    def __init__(self, name, price):
        self.name = name.replace("\'", "\'\'")
        self.price = int(price)

    def __str__(self) -> str:
        return f"{self.name} - ${self.price}"

    def __repr__(self) -> str:
        return f"MenuItem(name='{self.name}', price={self.price})"

    def cursor(self):
        return self._connection.cursor(cursor_factory=NamedTupleCursor)

    def save(self):
        with self.cursor() as cursor:
            query = f'''
            insert into {self._table_name} (item_name, item_price)
            values ('{self.name}', {self.price});
            '''
            cursor.execute(query)
            self._connection.commit()
            return cursor.rowcount

    def delete(self):
        with self.cursor() as cursor:
            # it feels like the logic insist that there 
            # should not be any items with the same item_name
            query = f'''
            delete from {self._table_name}
            where item_name = '{self.name}';
            '''
            cursor.execute(query)
            self._connection.commit()
            return cursor.rowcount

    def update(self, name=None, price=None):
        with self.cursor() as cursor:
            new_name = name if name else self.name
            new_price = price if price else self.price
            query = f'''
            update {self._table_name}
            set item_name = '{new_name}', item_price = {new_price}
            where item_name = '{self.name}';
            '''
            cursor.execute(query)
            self._connection.commit()
            self.name = new_name
            self.price = new_price
            return cursor.rowcount
