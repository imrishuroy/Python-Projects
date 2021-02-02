email = 'From rishukumar.prince@gmail.com Sat Nov 5 09:14:16 2020'

for line in email:
    line = line.rstrip()
    if not line.startswith('From ') : continue
    words = line.split()
    print(words)
    print(words[2])
print('Heelo')   


words = email.split()
print(words)
print(words[2])

w = email.split()
userEmail = w[1]
print(userEmail)
x = userEmail.split('@')
print(x[1])
