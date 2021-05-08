name = input("Enter file : ")
  if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

words = list()
count = dict()

for line in handle :
    line = line.split()
    if len(line) < 3 : continue
    if line[0] != 'From' : continue
    # print(line[1])
    words.append(line[1])
    # print(words)

# print(words)

for word in words :
    # print(words)
    count[word] = count.get(word, 0) + 1    

# print(count)       

bigcount = None
bigWord = None

for key,value in count.items():
    if bigcount is None or value > bigcount:
        bigWord = key
        bigcount = value

print(bigWord,bigcount)


