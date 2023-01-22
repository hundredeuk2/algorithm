from collections import deque

n = int(input())
n_edge = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(n_edge):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    
infested = [0] * (n+1)
infested[1] = 1

q = deque()
q.append(1)

while q:
    curr = q.popleft()
    
    for next_node in graph[curr]:
        if infested[next_node] == 1:
            continue
            
        elif infested[next_node] == 0:
            infested[next_node] += 1
            q.append(next_node)

cnt = 0            
for i in range(2,n+1):
    if infested[i] == 1:
        cnt += 1
        
print(cnt)