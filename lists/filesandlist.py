f = open('lists/email.txt')
for line in f:
    if not line.startswith('From '): 
        continue
    words = line.split('@')
    #print(words[2])
    #email = words[2]
    #val=email.split('@')
    #print(val)
    #print(val[1])
    print(words)