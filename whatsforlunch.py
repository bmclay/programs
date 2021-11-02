# Make a list of cuisine styles
cuisines = ['Pizza', 'Chinese', 'American', 'Italian', 'Mexican', 'Fast Food']

import random

# Lists of each resteraunt for each cuisine style
pizza = ['Pizza Joes', 'Foxs', 'Pizza Pie', 'Pizza Plus', 'Vocellis', 'Dominoes', 'Tanis', 'Anna Maries']
chinese = ['China Gourmet', 'China One', 'China Palace']
american = ['Monroe Hotel', 'Rachels Roadhouse', 'Chop Shop', 'Burger Hut', 'Texas Roadhouse', 'Upper Crust', 'Cannella Cafe', 'Hoagie Shop', 'Chilis', 'Applebees']
italian = ['Villa Grande', 'Mama Rosas']
mexican = ['Rey Azteca', 'Compadres']
fastfood = ['Mcdonalds', 'Arbys', 'Wendys', 'Burger King', 'Subway', 'KFC', 'Dairy Queen', 'Taco Bell']



# Print out a numbered list of the cuisine types
print('Select from the following options:')
for i, cuisine in enumerate(cuisines, 1):
    print('%d. %s' % (i,cuisine))

# Prompt the user to make a choice:
choice = input('Choose an option 1-6: ')

if choice == '1':
    print(random.choice(pizza))
elif choice =='2' :
    print(random.choice(chinese))
elif choice == '3' :
    print(random.choice(american))
elif choice == '4' :
    print(random.choice(italian))
elif choice == '5' :
    print(random.choice(mexican))
elif choice == '6' :
    print(random.choice(fastfood))
else:
    print('Try again')

