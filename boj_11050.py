n = list(map(int, input().split()))
f = 1
k = 1
for i,j in zip(range(n[0],n[0]-n[1],-1), range(n[1],-1,-1)):
    f *= i
    k *= j
print(int(f/k))