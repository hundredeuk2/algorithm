import sys
input = sys.stdin.readline

n = int(input())
names = []

for _ in range(n):
    names.append(input().split())
    
names.sort(key = lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for name in names:
    print(name[0])