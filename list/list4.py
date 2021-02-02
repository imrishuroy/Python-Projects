# algorigthm way of average

total = 0
count = 0

while True:
    inp = input('Enter a number : ')
    if inp == 'done' : break
    value = float(inp)
    total = total + value
    count = count + 1

average = total / count
print('Average', average)

# average by data-structure

numList = list()  # empty list or new list

while True:
    newInput = input('Enter a number : ')
    if newInput == 'done' : break
    newValue = float(newInput)
    numList.append(newValue)

averageNum = sum(numList) / len(numList)
print('Average ',averageNum)    
