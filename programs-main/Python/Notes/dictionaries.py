# Dictionaries are a key value pair
# Create the dictionary, assign it to a variable
x = {'key': 4}
# Later on in the code you can print the variables associated value by specifying the key (I just named it key)
print(x['key'])

# Add a new key
x['key2'] = 5
x[2] = [8, 2, 1, 3, 0]
print(x)

# Find out if something is in the dictionary x
print('key' in x)

# List all of the values
print(list(x.values()))

# List all of the keys
print(list(x.keys()))

# Delete a key
del x['key']
print(x)

# Loop over the dictionary. To pull the key and the value.
y = {'key': 100}
for key, value in y.items():
    print(key, value)

for key in y:
    print(key, y[key])