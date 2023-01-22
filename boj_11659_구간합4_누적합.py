import sys
input = sys.stdin.readline

n, m = map(int, input().split())

numbers = list(map(int, input().split()))

for idx in range(n-1):
    numbers[idx+1] += numbers[idx]
numbers = [0] + numbers

for _ in range(m):
    a,b = map(int,input().split())
    print(numbers[b]-numbers[a-1])
