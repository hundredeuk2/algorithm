def three(num, cnt):
    if len(num) < 2:
        x = int(num) % 3
        return cnt, x
    
    num = str(sum(list(map(int,num))))
    cnt += 1
    return three(num, cnt)

num = input()
cnt = 0

a = three(num,cnt)

if a[1] >=1 :
    print(a[0],"NO",sep='\n')
else :
    print(a[0],"YES",sep='\n')