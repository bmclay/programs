# Comparison operators. The result is always a boolean value (True or False)
# Can be used to compare floats and ints(float to float int to int or float to int or int to float):
# == is equal to. Check for equality
# != not equal to. Check for inequality
# <= less than or equal to
# >= greater than or equal to
# < less than
# > greater than
print(7.0 == 7)
print(7.0 != 7)
print(7.0 <= 7)
print(7.0 >= 7)
print(7.0 < 7)
print(7.0 < 7)
# These can be stored in variables
result = 6 == 6
print(result)



# Can be used to compare strings:
# == is equal to. Check for equality
# != not equal to. Check for inequality
# <= less than or equal to
# >= greater than or equal to
# < less than
# > greater than
x = 'hello'
y = 'hello'
z = 'bye'
# Compare two variable values
# Check for equality
print(x == y)
# Check for inequality
# In this case, the values are the same so False is returned.
print(x != y)
# In this case, the values are different, True is returned.
print(x != z)
# Characters
# All characters inside of python are represented by an ordinal value. 
# To show the ordinal value of a character.
print(ord('a'))
print(ord('z'))
# Show if one charachters ordinal value is greater than another.
print('a' > 'z')
# Show if one charachters ordinal value is less than another.
print('a' < 'z')
# Comparing multiple characters. This compares a to a, then b to d. b is not greater than d so False prints.
print('ab' > 'ad')


# Conditionals
x = 7
y = 8
z = 0

result1 = x == y
print(result1)
result2 = y > x
print(result2)
result3 = z < x + 2
print(result3)
# Arithmatic operators take presedence over comaprison operators, meaning all of the math on each side of the equation is conducted then the values on the left and right are compared.
result4 = x - 1 < x + 2
print(result4)

# Chained conditionals
# Keywords used: or | not | and
# Check to see if result4 is equal to either result1 or result2.
# result4 is true result1 is false but result2 is true so True is printed. False is only printed when both sides of or are False.
result5 = result1 or result2
print(result5)
# Chained conditionals can be taken multiple levels deep. If any are True, then true is printed
result6 = result1 or result3 or result4
print(result6)

# Flip boolean value by asking the expresion or not
result7 = result1 or not result2 or not result3
print(result7)

# not can be easily expressed by using print(not True) you are telling python to print not True which is False.
print(not True)
# Print not false will print true
print(not False)

# and: if both the left and right side are true then the entire statement is true.
print(True and True)

# Order of operations are not,then and, then or