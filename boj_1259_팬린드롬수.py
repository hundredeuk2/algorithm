def check(num):
    mid = len(num)//2
    for i in range(mid):
        if num[i] != num[-(i+1)]:
            return print("no")
    return print("yes")

while True:
    n = str(input())
    if n == "0":
        break
    check(n)
