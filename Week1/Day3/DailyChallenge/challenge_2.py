# Create a program that prints a list of the items you can afford in the store with the money you have in your wallet.
# Sort the list in alphabetical order.
# Return “Nothing” if you can’t afford anything from the store.

items_purchase = {
  "Water": "$1",
  "Bread": "$3",
  "TV": "$1,000",
  "Fertilizer": "$20"
}

wallet = "$1,004"
wallet = int(wallet.replace('$', '').replace(',', ''))
affordable_items = []

for key, val in items_purchase.items():
    item_cost = int(val.replace('$', '').replace(',', ''))
    if wallet >= item_cost:
        affordable_items.append(key)
        wallet -= item_cost

if len(affordable_items) > 0:
    print(sorted(affordable_items))
else:
    print('Nothing')


