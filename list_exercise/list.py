text = open('mbox-short.txt')

for line in text:
    line = line.rstrip()
    # if line = '' : 
    #     print('Skipped Blank Line')
    #     continue
    # print('Line', line)
    words = line.split()
    # print('Words', words)
    # Guardian Pattern
    if len(words) < 3 : continue
    if words[0] != 'From' : 
        # print('Ignore')
        continue
    print(words[2])