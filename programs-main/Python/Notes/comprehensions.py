# A one line initialization of a list, tuple, dictionary etc...
# Start at 0 count up 5 positions and assign this to x.
x = [x for x in range(5)]
print(x)

# Specify starting position and count up
x = [x + 5 for x in range(5)]
print(x)

# A list of all one charachter
x = [0 for x in range(5)]
print(x)

# Python will take what you have on the left of the for and apply with you have on the right of for.

# Create 5 lists of a list of ten 0s, assign this to variable x and print.
x = [[0 for x in range(10)] for x in range(5)]
print(x)

# Show all of the increments of 5 from 0 to 100
x = [i for i in range(100) if i % 5 == 0]
print(x)

# Do something similar but with a tuple instead
x =tuple(i for i in range(100) if i % 5 == 0)
print(x)