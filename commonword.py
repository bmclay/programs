# Use this to open a text file and print the most frequent used word in the file.

# Get the name of the file and open it
name = input('Enter file:')
handle = open(name, 'r')

# Count word frequency
counts = dict()
for line in handle:
        words = line.split()
        for word in words:
                counts[word] = counts.get(word,0) +1

# Find the most common word
bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = counts

# All done
print (bigword, bigcount)
