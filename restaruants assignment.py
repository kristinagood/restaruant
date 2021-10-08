vegetarian = input('Is anyone at your party vegetarian? ').lower()
vegan = input('Is anyone at your party vegan? ').lower()
gluten_free = input('Is anyone at your party gluten free? ').lower()
print('Here are your choices:')
while vegetarian != 'yes' and vegan != 'yes' and gluten_free != 'yes':
    print('Joes Gourmet Burgers')
    print('Main Street Pizza Company')
    print('Mamas Fine Italian')
while vegetarian != 'yes' and vegan != 'yes' and gluten_free == 'yes':
    print('Main Street Pizza Company')
while vegetarian == 'yes' and vegan != 'yes' and gluten_free == 'yes':
    print('Main Street Pizza Company')
while vegetarian == 'yes' and vegan != 'yes' and gluten_free != 'yes':
    print('Main Street Pizza Company')
    print('Mamas Fine Italian')

print('Corners Cafe')
print('The Chefs Kitchen')

start = 'yes'
stop = 'no'
restaurant_search = input('Would you like to do another restaurant search? :')
for x in range(vegetarian,vegan, gluten_free):
    print(loop)
