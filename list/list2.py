# list are mutable

# we can add two differents lists
a = [1,2,3,4,5]
b = [6,7,8,9,10]
c = a + b 
print(c)

# slicing in list
t = [9, 10, 11, 12, 13]
print(t[2 : 4])

# list from scratch

stuff = list()
stuff.append('book')
stuff.append(10)
print(stuff)

# in
some = [1, 3, 5, 7, 9, 11]
if 13 in some:
    print('Found')
else:
    print('Not Found')   
print(11 in some)

# not in
numbers = [1, 3, 5, 7, 9, 11]
if 13 not in numbers:
    print('Not in List')
else:
    print('Not Found')   
print(11 not in numbers)


#sort
friends = ['Rishu', 'Vinay', 'Nisi', 'Satyam']
friends.sort()
print(friends)


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9 ,10]
print(len(numbers))
print(sum(numbers))
print(min(numbers))
print(max(numbers))
print(sum(numbers) / len(numbers))
