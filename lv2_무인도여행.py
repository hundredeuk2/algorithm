def bfs (a, maps, visited):
    q = [a]
    dx, dy = [0,0,-1,1], [1,-1,0,0]
    
    m = len(maps[0])
    n = len(maps) 
    
    visited[a[0]][a[1]] = True
    cnt = int(maps[a[0]][a[1]])
    
    while q:
        x,y = q.pop(0)
        for i in range(4):
            
            nx, ny = x + dx[i], y + dy[i]
            
            if nx >= n or nx < 0 or ny >= m or ny < 0:
                continue 
            if visited[nx][ny]:
                continue
            if maps[nx][ny] == "X":
                continue
            
            q.append([nx,ny])
            cnt += int(maps[nx][ny])
            visited[nx][ny] = True
            
    return cnt, visited

def solution(maps):
    answer = []
    
    visited = [[False]*len(maps[0]) for _ in range(len(maps))]

    for i in range(len(maps)):
        tmp = maps[i]
        for j in range(len(tmp)):
            if visited[i][j]:
                continue

            if not maps[i][j] =="X":
                cnt, visited = bfs([i,j], maps, visited)
                answer.append(cnt)
    if not answer:
        return [-1]
    return sorted(answer)