n, k = map(int, input().split())

coin_l = []
for i in range(n) :
    coin_l.append(int(input()))
coin_l = sorted(coin_l, reverse=True)

count = 0
for j in coin_l :
    
    tmp_val = k // j        
    count += tmp_val
    k -= j * tmp_val
    if k == 0 :
        break
print(count)