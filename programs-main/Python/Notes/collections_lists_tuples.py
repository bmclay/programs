# Collections are an ordered or un ordered group of elements.
 
# lists are set using square brackets []
# inside of the square brackets you can have a series of elements (some data type).

# To define a list, create a variable and open up square brackets with some elements inside
x = [4, True, 'hi']
print(x)
# To print the length of the list, use the len function
print(len(x))
# The len function can also be used to count the total number of characters in a string
y = 'whats up'
print(len(y))
# Append to the end of the list
x.append('hello')
print(x)
# Add elements to the end of the list with extend
x.extend([4, 5, 6, 7])
print(x)
# Remove the element at the end of the list using pop (in this case 7 is removed)
x.pop()
print(x)
# Print what it would be removing by using pop with the print function (in this case its 6)
print(x.pop())
# If you print x again at this stage, 6 is gone.
print(x)

# Each item in a list contains an index number
# Indexes are assigned from left to right starting with the number 0, 1, 2, 3, 4 etc...
y = [100, 'easy', False]
# Show what value is contained in a specified index position in a list:
print(y[1])
# Print what is in position '0' and pop it from the list
print(y.pop(0))
# Then if you print the list, 100 is removed because it was first aka index of 0.
print(y)
# Change the value of an element in a list by specifying the variable, the index number and its new value:
x[0] = 'NEW'
print(x)
# Tell python that variable y now equals the value of x
y = x
# When you store a list to a variable, the variable stores only a reference to the list not a copy of it.
# Lists are mutable which means they can be changed.
print(x, y)
# You can make python make a copy of the list instead of just a referance by specifying [:]
y = x[:]
print(y)

# Tuples are similar to lists but they are immutable. They cannot be changed once they are defined.
# Tuples use round brackets instead of square brackets.
a = (0, 85, 'bingo', 72, True, 'Jimmy')
print(a)
# You cant change the list. It's immutable
# Example of trying to change the value of index position 1. This results in an error
a[0] = 5
