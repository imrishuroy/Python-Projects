#exercise
counts = dict()
names = ['Rishu', 'Prince', 'Nisi', 'Rishu','Satyam', 'Rishu']

for name in names:
    if name not in counts:
        counts[name] = 1
    else :
        counts[name] = counts[name] + 1

print(counts)            