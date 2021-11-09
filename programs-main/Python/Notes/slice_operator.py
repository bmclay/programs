# Take a slice of a collection like a string, list or tuple and do something with it.
# [start:stop:step]
# Start at the first value, stop at the second value, increment by the third value

# Make a few lists, assign them to variables:

x = [0,1,2,3,4,5,6,7,8,9,10]
y = ['hi', 'hey', 'yo', 'hello', 'hola']
s = "hello"

# create a variable sliced and assign only the specified slice of the elements in the list assigned to variable x.
sliced = x[0:10:2]
print(sliced)
# We do not have to include all three arguments. You may omit them to do certain things
# Here we just include a stop. This says start at the beginning top at the specified value.
sliced = x[:10]
print(sliced)
# The same thing, using the list of words, this stops at index position 4 which is hola. Everything up to but not including hola is displayed.
sliced = y[:4]
print(sliced)
# Start at specified value, stop at the end.
sliced = x[2:]
print(sliced)
# Start at the beginning of the list, stop at the end of the list and count down by 1 the list. This reverses the list.
sliced = x[::-1]
print(sliced)
# If you have a simple string to evaluate it will use the index of each individual character in the string.
sliced = s[::-1]
print(sliced)
# Only show every other character in a string:
sliced =s[::2]
print(sliced)