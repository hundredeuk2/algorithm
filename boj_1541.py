data = input().split('-')
num = []
for i in data:
    cnt = 0
    try: 
        cnt = eval(i)
    except:
        s = i.split('+')
        
        for j in s:
            cnt += int(j)
    num.append(cnt)
    
n = num[0]
for i in range(1, len(num)):
    n -= num[i]
print(n)