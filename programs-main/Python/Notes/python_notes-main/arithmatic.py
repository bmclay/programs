# Performing mathmatical operations in python.
# Numeric expressions are +, -, *, /, **, %
# You cannot perform every mathmatical operations on a string.
# One exception is *, which can be performed on a string.
# When combined with print, you can specify the amount of times the string will be printed.
print('hello ' *9)
# Numbers (int or float) can be assigned to variables and then used in mathmatical operations.
x = 9
y = 3.5
result = x - y
print(result)
# Python will show float by default, even on a whole number.
z = 8
a = 2
result = z / a
print(result)
# If you dont want the result to be a float, specify int.
num1 = 50
num2 = 25
result = int(num1 / num2)
print(result)
# Exponent: ** can be used to raise numbers to the power of a specified value
num3 = 10
num4 = 5
# Value of num3 to the power of the value of num4
result = num3 ** num4
print(result)
# Use integer division: // to remove all of the decimal points and return the integer value
# The real answer of 10 / 3 is 3.333333333333333, but floor division will take away everything right of the decimal point.
num5 = 10
num6 = 3
result = num5 // num6
print(result)
# Use mod: % to show ONLY the remainder after a division occurs
num7 = 10
num8 = 3
result = num7 % num8
print(result)
# Order of operation is important. Python follows the simple order of operations to evaluate expressions.
# To remember, use the acronym BEDMAS Brackets Exponenets Division Multiplication Addition Subtraction. Integer division and mod operators are last. 
# You can operate on user input with integers using the int function.
num = input('Number: ')
print(int(num) - 5)
# You can do the same with a float.
num = input('Number: ')
print(float(num) - 5)
# By default Python 3 will always print a floating point number during math:
print(10 / 2)