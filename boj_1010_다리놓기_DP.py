def itera(low, big):
    x = 1
    for num in range(low,big+1):
        if num == 0:
            num = 1
        x *= num
    return x

def combination(num1, num2):
    big = max(num1, num2)
    low = min(num1, num2)
    
    return int(itera(1,big) / (itera(1,low) * itera(1,big-low)))

n = int(input())
for i in range(n):
    a,b = map(int, input().split())
    answer = combination(a,b)
    print(answer)