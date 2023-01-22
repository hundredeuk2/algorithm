def bfs(map_list,x,y):
    dx, dy = [-1,1,0,0], [0,0,-1,1]
    q = [(x,y)]
    map_list[x][y] = 0
    cnt = 1
    while q:
        x, y = q.pop(0)
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0<= nx < n and 0<= ny < n and map_list[nx][ny] == 1 :
                q.append([nx, ny])
                map_list[nx][ny] = 0
                cnt += 1
    return cnt

n = int(input())

map_list = [list(map(int,input())) for i in range(n)]

count = [bfs(map_list, i, j) for i in range(n) for j in range(n) if map_list[i][j] == 1]

count.sort()
print(len(count))

for i in range(len(count)):
    print(count[i])