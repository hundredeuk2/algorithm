import math

n = int(input())

for _ in range(n):
    m = int(input())
    wear = {}
    cnt = 1
    for _ in range(m):
        x, y = map(str,input().split(' '))
        if y in wear :
            wear[y] += 1
        else :
            wear[y] = 1
    
    num_list = list(wear.values())
    for num in num_list :
        cnt *= num+1
    print(cnt-1)
    