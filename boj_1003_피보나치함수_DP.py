n = int(input())

def fib(n):
    table = [1,1]
    cnt = [[1,0],[0,1]]
    for i in range(2,n+1):
        cnt.append([x + y for x, y in zip(cnt[i-2],cnt[i-1])])
    return print(cnt[n][0],cnt[n][1])

for _ in range(n):
    x = int(input())
    fib(x)