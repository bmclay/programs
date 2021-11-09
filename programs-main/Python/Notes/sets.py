# An un-ordered, unique collection of elements.
# Used when you care if something exists or not. Not when you're concerned with the frequency or order.
# Create a set
x = set()
# Create a set that has elements inside of it. This is a set literal. Notice duplicates are not displayed.
s = {1,1,1,1,114,104,23,123,1,40}
print(s)
# Add an element to the set
s.add(5)
print(s)
# Remove an element from the set
s.remove(1)
print(s)
# Ask if a value is a part of a set. Returns Boolean True if its there, False if its not.
print(33 in s)
# define another set to a variable s2, combine it with the set defined in s and print.
s2 = [2,45,123,304,100]
print(s.union(s2))
# show the difference between two sets
print(s.difference(s2))
# you can also show the intersection and symmetric difference etc...