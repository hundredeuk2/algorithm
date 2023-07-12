n = int(input())
map_list = []
M = 0

for _ in range(n):
    tmp = list(map(int, input().split()))
    M = max(M, max(tmp))
    map_list.append(tmp)
    
def bfs(x,y,M):
    q = [(x,y)]
    visited[x][y] = True
    dx, dy = [-1,1,0,0], [0,0,-1,1]
    while q:
        x,y = q.pop(0)
        for j in range(4):
            nx, ny = dx[j] + x, dy[j] + y
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if map_list[nx][ny] <= M :
                continue
            if visited[nx][ny] == True:
                continue
            q.append((nx,ny))
            visited[nx][ny] = True

answer = 0
for i in range(M):
    visited = [[False for _ in range(n)] for _ in range(n)]
    cnt = 0
    
    for x in range(n):
        for y in range(n):
            if map_list[x][y] > i and visited[x][y] == False :
                bfs(x,y, i)
                cnt += 1
    answer = max(answer, cnt)
print(answer)