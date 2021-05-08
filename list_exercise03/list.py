fname = input('Enter file name : ')

count = 0

text = open(fname)
for line in text:
    line = line.rstrip()
    line = line.split()
    if len(line) < 3 : continue
    if line[0] != 'From' : continue
    print(line[1])
    count = count + 1    
print('There were', str(count) + ' lines in the file with From as the first word')