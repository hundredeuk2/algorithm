n = int(input())

def fac (num):
    if num <= 1 :
        return 1
    return fac(num-1) * num

print(fac(n))