# add key pocket and add value

inventory = {
'gold' : [500],
'pouch' : ['flint', 'twine', 'gemstone'],
'backpack' : ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}

inventory["pocket"] = ["​seashell", "strangeberry" , "lint"]
print(inventory)


# remove​ 'dagger'​ from the list of items stored under the ​'backpack'​ key.
a = inventory.get("backpack")
a.pop(1)
print(inventory)

print("------")

# Add 50 to the number stored under the ​'gold'​ key.
add= inventory.get("gold")
add.append("50")
print(inventory)