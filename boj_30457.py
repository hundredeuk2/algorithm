n = int(input())
l = list(map(int, input().split(" ")))
dic = {x:0 for x in set(l)}
cnt = 0
for x in l:
    if dic[x] < 2:
        dic[x] += 1
        cnt += 1
print(cnt)