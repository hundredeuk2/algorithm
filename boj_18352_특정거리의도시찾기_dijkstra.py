import heapq
import sys

input = sys.stdin.readline

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
INF = int(1e9)
dist = [INF] * (n+1)


for i in range(m):
    a, b = map(int,input().split())
    graph[a].append((b,1))
    
def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    dist[start] = 0
    
    while q :
        n_dist, curr = heapq.heappop(q)
        # visited 확인
        if dist[curr] < n_dist:
            continue
        for i in graph[curr]:
            cost = n_dist + i[1]
            
            if cost < dist[i[0]]:
                dist[i[0]] = cost
                heapq.heappush(q, (cost,i[0]))
dijkstra(x)

if k in dist:
    for i in range(n+1):
        if dist[i] == k:
            print(i)
else:
    print(-1)        