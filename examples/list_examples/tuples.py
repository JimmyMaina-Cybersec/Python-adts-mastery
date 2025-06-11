menu = ("appetizers", "soups & salads", "main dish", "side dish")

print("Our restaurant offer various food types, some including:")
for food_type in menu:
    print(food_type)

"""Tuples are immutable
    TypeError: 'tuple' object does not support item assignment
"""
try:
    menu[1] = "dessert"
except TypeError:
    print("\nTuples are immutable!")


menu = ("appetizers", "dessert", "main dish", "beverages")
print("\nOur restaurant has changed the food types it offers. Here is our new menu:")
for food_type in menu:
    print(food_type)
