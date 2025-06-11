pizzas = [
    "neapolitan",
    "margherita",
    "sicilian",
    "buffalo",
    "hawaiian",
    "white",
    "california",
]

# Print the first three pizzas
print(f"These are the first three pizzas: {pizzas[:3]}\n")

# Print the three middle pizzas
print(f"These are the three middle-placed pizzas: {pizzas[2:5]}\n")

# Print the last three pizzas
print(f"These are the last three pizzas: {pizzas[-3:]}\n")

# Make a copy of the list of pizzas
friend_pizzas = pizzas[:]

# Add a pizza to pizzas
pizzas.append("detroit-tyle")

# Proof I have two separate lists
# print(f"Original: {pizzas}\nFriend's pizzas: {friend_pizzas}\n")
print("My favourite pizzas include:")
for pizza in pizzas:
    print(f"{pizza}")

print("\nMy friend's favourite pizzas include:")
for pizza in friend_pizzas:
    print(f"{pizza}")
