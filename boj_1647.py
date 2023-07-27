def find_parent(parent, x):
    if parent[x] != x:
        x = find_parent(parent, parent[x])
    return parent[x]

def union(parent, x, y):
    a = find_parent(parent,x)
    b = find_parent(parent,y)
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n ,m = map(int, input().split())
parent = [x for x in range(n+1)]
q = []
answer = 0
for _ in range(m):
    a,b,c, = map(int, input().split())
    q.append((c,a,b))

q.sort()
M = 0

for e in q:
    c, a, b = e
    if find_parent(parent, a) != find_parent(parent, b):
        union(parent,a,b)
        M = c
        answer += c

print(answer-M)
    