name = input('Enter file name : ')
handle = open(name)

counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0) + 1


#print(counts)


bigcount = None
bigWord = None

for key,value in counts.items():
    if bigcount is None or value > bigcount:
        bigWord = key
        bigcount = value

print(bigWord,bigcount)


