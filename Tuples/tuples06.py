# sorting list of tuples

d = {'a': 10, 'b': 1, 'c': 22}

e = d.items()
print(e)

f = sorted(e)
print(f)

# sort by value instead of key

c = {'a': 10, 'b': 1, 'c': 22}

tmp = list()

for k, v in c.items():
    tmp.append((v, k))

print(tmp)

tmp = sorted(tmp, reverse=True)
print(tmp)
# big to small(decending order)
