# In the file menu_manager.py, create a new class called MenuManager
# Create a Class Method called get_by_name that will return a single item from the Menu_Items 
# table depending on it’s name, if an object is not found (there is no item matching the name in 
# the get_by_name method) return None.

# Create a Class Method called all_items which will return a list of all the items from the Menu_Items table.

from restaurant_connection import restaurant_connection
from menu_items import MenuItem
from psycopg2.extras import NamedTupleCursor

class MenuManager:
    _table_name = 'menu_items'
    _connection = restaurant_connection
    # _cursor = restaurant_connection.cursor(cursor_factory=NamedTupleCursor)

    def __init__(self) -> None:
        pass
    
    @classmethod
    def cursor(cls):
        return cls._connection.cursor(cursor_factory=NamedTupleCursor)

    @classmethod
    def get_by_name(cls, name):
        with cls.cursor() as cursor:
            query = f'''
            select * from {cls._table_name} where item_name = '{name}' limit 1;
            '''
            cursor.execute(query)
            result = cursor.fetchone()
            if not result:
                return 
            return MenuItem(name=result.item_name, price=result.item_price)
    
    @classmethod
    def get_all_items(cls):
        with cls.cursor() as cursor:
            cursor.execute(f'select * from {cls._table_name};')
            return [MenuItem(name=item.item_name, price=item.item_price) for item in cursor.fetchall()]
    

def main():
    cursor = restaurant_connection.cursor()
    cursor.execute(f'truncate table {MenuItem._table_name}')
    restaurant_connection.commit()

    item = MenuItem('Burger', 35)
    item.save()
    item.delete()

    item = MenuItem('Mom\'s Spagetti', 99)
    item.save()
    item.update('Italial Meatballs', 44)

    item = MenuItem('Beef Stew', 14)
    item.save()
    
    item = MenuManager.get_by_name('Beef Stew')
    print('Beef Stew query: ', item)

    item = MenuManager.get_by_name('Boof Stew')
    print('Boof Stew query: ',item)

    items = MenuManager.get_all_items()
    print(items)

    restaurant_connection.close()

if __name__ == '__main__':
    main()
