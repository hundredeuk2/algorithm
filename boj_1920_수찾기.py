import sys
input = sys.stdin.readline

n = int(input())
org_list = list(map(int, input().split()))
m = int(input())
target_list = list(map(int, input().split()))

else_list = set(target_list) - set(org_list)
for num in target_list:
    if num in else_list:
        print(0)
    else:
        print(1)