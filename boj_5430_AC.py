import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    orders = str(input())
    n = int(input())
    num_list = input().rstrip()[1:-1].split(',')
    
    err = 0
    r = 0
    for order in orders :
        if order == "R":
            r += 1
        elif order == "D":
            if len(num_list) < 1 or n == 0:
                err += 1
                break
            elif r % 2 == 0:
                num_list.pop(0)
            elif r % 2 == 1:
                num_list.pop()
    
    if err == 1:
        print("error")
    elif r % 2 == 1:
        num_list.reverse()
        print("[" + ",".join(num_list) + "]")
    else:
        print("[" + ",".join(num_list) + "]")