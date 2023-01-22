import sys
input = sys.stdin.readline

n, m = map(int, input().split())
num_list = list(map(int, input().split()))

num_list.sort()

visited = [False] * n
arr = []
def dfs(num):
    if len(arr) == num:
        print(*arr)
        return
    for i in range(n):
        if visited[i]:
            continue
        visited[i] = True
        arr.append(num_list[i])
        
        dfs(num)
        
        arr.pop()
        visited[i]=False
dfs(m)
