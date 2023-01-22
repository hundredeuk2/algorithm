def cnt(a,b):
    c = 0
    for i in range(2):
        if a[i] < b[i]:
            c += 1
    return c // 2

n = int(input())
peoples = []
for _ in range(n):
    peoples.append(list(map(int, input().split(' '))))

answers = []
for i in range(n):
    diff = 1
    for j in range(n):
        diff += cnt(peoples[i], peoples[j])
    answers.append(diff)
    
print(*answers)