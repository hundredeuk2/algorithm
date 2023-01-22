from collections import deque

M, N  = map(int,input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

dx, dy = [1,-1,0,0],[0,0,1,-1]

def bfs(graph, q):
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                q.append([nx,ny])


q = deque([])
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            q.append((i,j))
            
bfs(graph,q)
result = 0
for i in graph:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    result = max(result, max(i))
print(result -1)