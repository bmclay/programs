# For loops are loops that iterate a set amount of times
# 
# Demonstrated below with the range function. range creates a collection of numbers based on the numbers we give it.
# range will accept up to 3 comma separated numbers defined as:
# Start, Stop, Step

# If just one argument is specified, 
# Stop: Start at zero and go up by 1 until you reach that count. 
# In the example below, 10 is specified so 0 - 9
for i in range(10):
    print(i)
print('Done')
# If we have two arguments,
# Start, Stop: Start at the first specified number and go to the second specified number.
# In this example, 1 and 10 is specified so 1 - 10
for i in range(1, 10):
    print(i)
print('Done')
# If 3 arguments are specified,
# Start, Stop, Step: Start at the 1st number, end at the 2nd number, incrementing by the 3rd number.
for i in range(10, 0, -1):
    print(i)
print('Blastoff!')
# The loop will do nothing if you specify an invalid start, stop step
for i in range(-10, -1, -1):
        print(i)
print('fail')

# Using lists with for loops
# This will print the list in the square brackets in order from left to right.
for i in [2, 43, 2, 21, 91]:
    print(i)
print('Done with first list')
# Keep track of what index you are at by specifying a variable and storing the list in it, and using the len function
x = [2,4,6,422,6,103,1]
for i in range(len(x)):
    print(x[i])
print('Done with second list')
# Create indexes and values for each of the elements in the list
for i, element in enumerate(x):
    print(i, element)