name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)


words = list()
count = dict()
hlist = []

for line in handle:
    line = line.split()
    if len(line) < 3 : continue
    if line[0] != 'From' : continue
    h = line[5].split(':')
    # words.append(line[5].split(':'))
    count[h[0]] = count.get(h[0], 0) + 1

    
# print(count)

for k, v in count.items():
    hlist.append((k, v))

hlist.sort()
for k, v in hlist:
    print(k, v)    










   