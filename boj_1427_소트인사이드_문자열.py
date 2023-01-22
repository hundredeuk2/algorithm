n = list(map(int,input()))

x = sorted(n,reverse=True)

value = ''
for i in x:
    value += str(i)
    
print(int(value))