import sys
n = int(sys.stdin.readline())

s = []

for i in range(n):
    order = sys.stdin.readline().split()
    
    if order[0] == "push":
        s.append(int(order[1]))
    elif order[0] == "pop":
        if len(s) >= 1:
            print(s.pop())
        else:
            print(-1)
    elif order[0] == "size":
        print(len(s))
        
    elif order[0] == "empty":
        if len(s) >= 1 :
            print(0)
        else:
            print(1)
    elif order[0] == "top":
        if len(s) >= 1:
            print(s[-1])
        else :
            print(-1)