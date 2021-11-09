# Strings
# Using the type function when combined with print will show the class or type of the variable.
hello = 'hello'
print(type(hello))
#String Methods
# String Methods are operations you can perform on a string that will change the output displayed based on the method specified
hello = 'hello'
print(hello.upper())
print(hello.lower())
print(hello.capitalize())
# Look for a specified string within a string and count the matching occurances.
print(hello.count('ll'))
# Be aware here that lowercase letters do not equal uppercase letters
hello = 'heLLo World'
# count will show 0 here because there are no lower case ll or no match for ll.
print(hello.count('ll'))
# to get around this, modify prints output by converting the string to lowercase with the lower method.
print(hello.lower().count('ll'))
# String Multiplication and addition
x = 'hello'
y = 'Bill'
# Repeat a string by multiplying
print(x *10)
# Concatenate two strings
print(x + y)

# Floats
# Make a floating point number:
print(float(99))
# Python 3 will always print a floating point number during math
print(10/2)

# String Conversion
# Create a string containing 123 and assign it to variable a
a = '123'
# This will print the type, str because we enclosed 123 in quotes
print(type(a))
# create a variable b and load the int value of a into it
b = int(a)
# This will print <class 'int'> since b was assigned the int value of a
print(type(b))
# Add 1 to b which contrains the integer value of a 123. 1 + 123 = 124
print(b+1)
