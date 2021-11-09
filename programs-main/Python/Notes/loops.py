#Example of a while loop (Indefinite Loop)
n = 5
while n > 0 :
    print(n)
    n = n - 1
print('Blastoff!!!')

#Example of a definate loop with for 
for i in [5, 4, 3, 2, 1] :
    print(i)
print('Blastoff!!!')

#Finding the Average in a Loop
count = 0
sum = 0
print('Before', count, sum)
for value in [9, 41, 12, 3, 74, 15] :
    count = count + 1
    sum = sum + value
    print(count, sum, value)
print('After', count, sum, sum /count)

#Example of a loop using a boolean variable
found = False
print('Before', found)
for value in [9, 41, 12, 3, 74, 15] :
    if value == 3 :
        found = True
        break
    print(found, value)
print('After', found)

#Example of a loop using a None type variable
#Here None represents the smallest number in the value list
smallest = None
print('Before')
for value in [9, 41, 12, 3, 74, 15] :
    if smallest is None :
        smallest = value
    elif value < smallest :
        smallest = value
    print(smallest, value)
print('After', smallest)
