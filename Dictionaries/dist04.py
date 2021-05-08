# get method

counts = dict()
name = 'Rishu'
counts['Rishu'] = 91

if name in counts:
    x = counts[name]
else :
    x = 0 
print(x)

# get function

newNames = dict()
y = newNames.get('Rishu', 0)
# default value if key dont exist and no traceback
print(y)