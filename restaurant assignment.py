def ResturantSelector():
    resturants =(['Joes Gourmet Burgers','no','no','no'],['Main Street Pizza Company','yes','no','yes'],['Corner Cafe','yes','yes','yes'],['Mamas Fine Italian','yes','no','no'],['The Chefs Kitchen','yes','yes','yes'])
    vegetarian = input('Is anyone at your party vegetarian? ')
    vegan = input('Is anyone at your party vegan? ')
    gluten_free = input('Is anyone at your party gluten free?')
    print('Here are your choices:')
    for x in resturants:
        if vegetarian == 'yes' and x[1] =='no':
            continue
        if vegan == 'yes' and x[2] == 'no':
            continue
        if gluten_free == 'yes' and x[3] == 'no':
            continue
        print('\t',x[0])
ResturantSelector()
