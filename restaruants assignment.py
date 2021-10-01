vegetarian = input('Is anyone at your party vegetarian? ').lower()
vegan = input('Is anyone at your party vegan? ').lower()
gluten_free = input('Is anyone at your party gluten free? ').lower()
print('Here are your choices:')
if vegetarian != 'yes' and vegan != 'yes' and gluten_free != 'yes':
    print('Joes Gourmet Burgers')
    print('Main Street Pizza Company')
    print('Mamas Fine Italian')
if vegetarian != 'yes' and vegan != 'yes' and gluten_free == 'yes':
    print('Main Street Pizza Company')
if vegetarian == 'yes' and vegan != 'yes' and gluten_free == 'yes':
    print('Main Street Pizza Company')
if vegetarian == 'yes' and vegan != 'yes' and gluten_free != 'yes':
    print('Main Street Pizza Company')
    print('Mamas Fine Italian')
print('Corners Cafe')
print('The Chefs Kitchen')
