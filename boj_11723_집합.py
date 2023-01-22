import sys
input = sys.stdin.readline

n = int(input())

s = set()
for _ in range(n):
    orders = input().strip().split()
    
    if len(orders) == 1:
        if orders[0] == "all":
            s = set([x for x in range(1, 21)])
        else:
            s = set()
    else : 
        order, num = orders[0], int(orders[1])
        if order == "add" :
            s.add(num)
        elif order == "remove":
            s.discard(num)
        elif order == "check":
            if num in s:
                print(1)
            else :
                print(0)
        elif order == "toggle":
            if num in s :
                s.discard(num)
            else:
                s.add(num)