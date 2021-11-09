# Variables assign a name to some kind of data type
name = 'bill'
# Once its assigned it can be used by passing the variable through a function
print(name)
# You can set variables to another variable
var = name
print (name, var)
# Python reads top to bottom, so if you name a variable again, it wont be reflected until that point in the code.
city = 'Butler'
town = 'town'
print(town)
town = city
print(city, town)
# Variable naming conventions
# Special characters and spaces cannot be used in variable name (_ underscores are ok)
# You cannot start a variable with a number
