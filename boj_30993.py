def fact(num):
    tmp = num
    for i in range(1, num):
        tmp *= i
    return tmp

n,a,b,c = map(int, input().split())
anchor = fact(n)
for x in [a,b,c]:
    tmp = fact(x)
    anchor /= tmp
print(int(anchor))