fname = input('Input file name : ')

newList = list()
req = list()
text = open(fname)

for line in text:
    line = line.rstrip()
    words = line.split()
    for i in words:
        if i in newList : continue
        newList.append(i)
newList.sort()
print(newList)
# for i in newList:
#     if i in req : 
#         continue
#     req.append(i)
# print(req)


    #req.append(newList)
    #print(req)
# print(req)


#print(newList)
