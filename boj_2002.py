n = int(input())
inner = []
for i in range(n):
    tmp = str(input())
    inner.append([tmp,i])
    
outter = []
for i in range(n):
    tmp = str(input())
    outter.append(tmp)

q = []
i = 0
cnt = 0
for i in range(n):
    tmp, index = inner[i]
    if tmp in q:
        cnt += 1
        continue
    
    if outter[i] != tmp:
        for j in range(n):
            if outter[j] == tmp:
                break
        q.extend(outter[i:j])
print(cnt)