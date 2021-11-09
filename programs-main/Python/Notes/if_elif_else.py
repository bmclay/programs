# If elif else

# Here you define user input and assign it to variable x.
x = input ('Name: ')
# Begin the statement with if, you may have as many if statements as you would like.
# Indentation is part of the syntax, ex:
# If this thing
    # Do that thing
# Indentation is 4 spaces (not a typical tab). Most IDEs and text editors have this already set like this but you may have to go into settings to check it if you get tracebacks complaining about it.
if x == 'Bill':
    print('Hey Bill!')
elif x == 'Joe':
    print('Hey Joe')
else:
    print('Hello new user')

    