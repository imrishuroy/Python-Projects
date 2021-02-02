#for loop in dictonary

counts = {'Rishu': 1, 'Nisi': 10, 'Satyam': 20, 'Yogi': 100, 'Vinay': 200}

for key in counts:
    print(key, counts[key])



# Retrieving list of keys and values

jjj = {'Ram' : 21, 'Shyam': 100, 'Shita': '200', 'John':  45}

#list from dictionary
print(list(jjj)) 

#list of keys
print(jjj.keys())

#list of values
print(jjj.values())

#list of items
print(jjj.items())