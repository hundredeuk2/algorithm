n,m  = map(int,input().split())
map_list = []
for _ in range(n):
    map_list.append(list(map(int,input().split())))
    
def bfs(x,y, visited):
    q = [(x,y)]
    visited[x][y] = True
    dx, dy = [1,-1,0,0], [0,0,1,-1]
    size = 1
    while q:
        x,y = q.pop(0)
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if nx >= n or nx < 0 or ny >= m or ny < 0:
                continue
            if map_list[nx][ny] == 0 :
                continue
            if visited[nx][ny]:
                continue
            q.append((nx,ny))
            visited[nx][ny] = True
            size += 1
    return size
    
visited = [[False]*m for _ in range(n)]
scale = 0
cnt = 0
for i in range(n):
    for j in range(m):
        if map_list[i][j] == 1 and visited[i][j] == False:
            tmp = bfs(i,j, visited)
            scale = max(scale, tmp)
            cnt += 1
print(cnt)
print(scale)
