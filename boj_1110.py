#완
num = int(input())

def cal (num):
    if num < 10:
        num = str(num).zfill(2)
    else :
        num = str(num)
    new_front_num = num[1]
    new_back_num = int(num[0])+int(num[1])
    if new_back_num < 10:
        new_back_num = str(new_back_num).zfill(2)[1]
    else :
        new_back_num = str(new_back_num)[1]
        
    num = int(new_front_num+new_back_num)
    
    return num

count = 1
init_num = num
one_num = cal(num)

while init_num - one_num != 0:
    one_num = cal(one_num)
    count += 1
    
print(count)