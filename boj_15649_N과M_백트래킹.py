import sys
input = sys.stdin.readline

n,m = map(int, input().split())

num_list = [i+1 for i in range(n)]
visited = [False] * n

arr = []

def dfs(cnt) :
    if cnt == m:
        print(*arr)
        return
    for i in range(n):
        if visited[i]:
            continue
        visited[i] = True
        arr.append(num_list[i])
        
        dfs(cnt+1)
        
        arr.pop()
        visited[i] = False
dfs(0)