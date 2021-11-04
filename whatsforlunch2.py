# The program that picks where we are going to eat lunch!

# Make the lists
syles = ['Pizza', 'Chinese', 'American', 'Italian', 'Mexican', 'Fast Food']

# Lists of each resteraunt for each cuisine style
pizza = ['Pizza Joes', 'Foxs', 'Pizza Pie', 'Pizza Plus', 'Vocellis', 'Dominoes', 'Tanis', 'Anna Maries']
chinese = ['China Gourmet', 'China One', 'China Palace']
american = ['Monroe Hotel', 'Rachels Roadhouse', 'Chop Shop', 'Burger Hut', 'Texas Roadhouse', 'Upper Crust', 'Cannella Cafe', 'Hoagie Shop', 'Chilis', 'Applebees']
italian = ['Villa Grande', 'Mama Rosas']
mexican = ['Rey Azteca', 'Compadres']
fastfood = ['Mcdonalds', 'Arbys', 'Wendys', 'Burger King', 'Subway', 'KFC', 'Dairy Queen', 'Taco Bell']

# Give the user some context.
print("\nPlease make a selection:")

# Set an initial value for choice other than the value for 'quit'.
choice = ''

import random

# Start a loop that runs until the user enters the value for 'quit'.
while choice != 'q':
    # Give all the choices in a series of print statements.
    print("\n[1] Pizza")
    print("[2] Chinese")
    print("[3] American")
    print("[4] Italian")
    print("[5] Mexican")
    print("[6] Fast food")
    print("[q] Enter q to quit.")
    
    # Ask for the user's choice.
    choice = input("\nWhat style would you like? ")
    
    # Respond to the user's choice.
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
        print('Invalid choice, Try again')
        
# Print a message that we are all finished.
print("Enjoy your lunch!")
