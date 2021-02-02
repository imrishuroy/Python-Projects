for i in [5, 10, 12, 19]:
    print(i)
print('BlastOff')    

friends = ['Ram', 'Shayam', 'Shita', 'Geeta']
for friend in friends:
    print('Happy new year', friend)
print('Done')    

names = ['Rishu', 'Yogi', 'Nisi', 'Satyam', 'Vinay']
names[0] = 'Prince' # because list are mutable
print(names[0])

lotto = [12, 24, 23, 786, 23, 89]
print(lotto)
print('After list mutating')
lotto[2] = 25
print(lotto)


# len() - gives the length of string or list



greet = 'Hello Rishu'
print(len(greet)) # len() function in string

z = [1, 3, 'Bob' , 3.0, 'Print']
print(len(z))  # len() function with list


