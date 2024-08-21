# Create a file called menu_editor.py , which will have the following functions:


from menu_items import MenuItem
from menu_manager import MenuManager



def view_item_from_menu():
    item_name = input('Please enter the item name: ')
    item = MenuManager.get_by_name(item_name)
    if item:
        print(item)
    else:
        print('Item not found')

def add_item_to_menu():
    item_name = input('Please enter the item name: ')
    item_price = input('Please enter the item price: ')
    item = MenuItem(item_name, item_price)
    if item.save() == 1: # checks the rowcount
        print('Item was added successfully')
    else:
        print('Error: Item was not added')

# remove_item_from_menu()- this function should ask the user to input the name of the item they want to remove from the restaurant’s menu. This function will not interact with the menu itself, but simply create a MenuItem object and call the appropriate function from the MenuItem object.
# If the item was deleted successfully – print a message to let the user know this was completed.
# If not – print a message which states that there was an error.
def remove_item_from_menu():
    item_name = input('Please enter the name of the item you want to remove: ')
    item = MenuItem(item_name, 0)
    if item.delete() == 1: # checks the rowcount
        print('Item was removed successfully')
    else:
        print('Error: Item was not removed')

# update_item_from_menu()- this function should ask the user to input the name and price of the item they want to update from the restaurant’s menu, as well as to input the name and price they want to change them with. This function will not interact with the menu itself, but simply create a MenuItem object and call the appropriate function from the MenuItem object.
# If the item was updated successfully – print a message to let the user know this was completed.
# If not – print a message which states that there was an error.
def update_item_from_menu():
    # Don't understand why we need the price of the item. 
    old_name = input('Please enter the name of the item you want to update: ')
    old_item = MenuItem(old_name, 0)
    new_name = input('Please enter the new name of the item: ')
    new_price = input('Please enter the new price of the item: ')
    if old_item.update(new_name, new_price) == 1: # checks the rowcount
        print('Item was updated successfully')
    else:
        print('Error: Item was not updated')


# show_restaurant_menu() - print the restaurant’s menu.
def show_restaurant_menu():
    for i, item in enumerate(MenuManager.get_all_items()):
        print(f'{i+1}. {item}')

# show_user_menu() - this function should display the program menu (not the restaurant menu!), and ask the user to :
# View an Item (V)
# Add an Item (A)
# Delete an Item (D)
# Update an Item (U)
# Show the Menu (S)
# Call the appropriate function that matches the user’s input.
def display_options():
    print(
        'Please choose an option:',
        'V - View an Item',
        'A - Add an Item',
        'D - Delete an Item',
        'U - Update an Item',
        'S - Show the Menu',
        'E - Exit',
        sep='\n'
    )


def show_user_menu():
    while True:
        display_options()
        choice = input().upper()
        if choice == 'V':
            view_item_from_menu()
        elif choice == 'A':
            add_item_to_menu()
        elif choice == 'D':
            remove_item_from_menu()
        elif choice == 'U':
            update_item_from_menu()
        elif choice == 'S':
            show_restaurant_menu()
        elif choice == 'E':
            exit()
        else:
            print('Invalid option. Please try again.')


if __name__ == '__main__':
    show_user_menu()