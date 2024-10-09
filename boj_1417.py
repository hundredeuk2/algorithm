def search(l):
    max_value = max(l)
    return l.index(max_value)

n = int(input())
whobo = [int(input()) for _ in range(n)]
cnt = 0

if len(whobo) <= 1:
    print(0)
    exit(0)
    
while True:
    if max(whobo[1:]) < whobo[0]:
        break
        
    idx = search(whobo[1:]) + 1

    whobo[idx] -= 1
    whobo[0]+= 1
    cnt += 1

print(cnt)