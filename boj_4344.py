n = int(input())

def cal (x):

    mid = sum(x[1:]) / (len(x)-1)
    count = 0
    for i in range(1,len(x)):
        if x[i] > mid :
            count += 1
    return "{:.3f}%".format(count/x[0]*100)

for i in range(n):
    num_list = list(map(int,input().split()))
    print(cal(num_list))