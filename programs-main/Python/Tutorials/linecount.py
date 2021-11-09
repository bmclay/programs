# Open a file to work with
filename = input('Specify the file path for the file to open: ')
try:
    fhand = open(filename)
except:
    print('File cannot be opened:', filename)
    quit()

# Prime the loop to start at 0
count = 0
for line in fhand:
    count = count + 1
print('Line Count:', count)
