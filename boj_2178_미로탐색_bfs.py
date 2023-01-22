N, M = map(int,input().split())

maze = []
for _ in range(N):
    tmp = str(input())
    maze.append(tmp)
    
dx, dy = [1,-1,0,0], [0,0,1,-1]
visited = [[False] * (M) for _ in range(N)]
count = [[0] * (M) for _ in range(N)]


q = [[0,0]]
visited[0][0] = True
count[0][0] = 1

while q:
    x, y = map(int, q.pop(0))
    cnt = count[x][y] + 1
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        
        if 0 <= nx < N and 0<= ny < M and maze[nx][ny]== "1" and visited[nx][ny] == False:
            count[nx][ny] = cnt
            visited[nx][ny] = True
            q.append([nx,ny])             
print(count[N-1][M-1])