def fn(n):
    if n == 0:
        return "-"
    return fn(n-1) + " "* 3**(n-1) + fn(n-1)

while True:
    try:
        x = int(input())
        print(fn(x))
    except:
        break