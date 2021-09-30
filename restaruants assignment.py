vegetarian = input('Is anyone at your party vegetarian? ')
vegan = input('Is anyone at your party vegan? ')
gluten_free = input('Is anyone at your party gluten free? ')
print('Here are your choices:')
if not vegetarian and not vegan and not gluten_free:
    print('Joes Gourmet Burgers')
elif vegetarian and vegan and gluten_free:
    print('Corners Cafe')
    print('The Chefs Kitchen')
elif vegetarian and not vegan and gluten_free:
    print('Main Street Pizza Company')
elif vegetarian and not vegan and not gluten_free:
    print('Mamas Fine Italian')
