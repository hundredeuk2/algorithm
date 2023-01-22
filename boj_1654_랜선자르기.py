import sys
input = sys.stdin.readline

n, m = map(int, input().split())

lines = []
for _ in range(n):
    lines.append(int(input()))

end = max(lines)
start = 0

result = 0
while (start <= end):
    total = 0
    mid = (start+end) // 2
    for x in lines:
        if mid == 0:
            total += (x // 1)
        else:
            total += (x // mid)
    if total < m :
        end = mid - 1
    else :
        result = mid
        start = mid + 1
print(result)