num_list = list(map(int, input().split()))

res = False
for i in num_list :
    dup = num_list.count(i)
    if dup == 3 :
        print(10000+(i*1000))
        res = True
        break
    if dup == 2 :
        print(1000+(i*100))
        res = True
        break

if res == False :
    print(max(num_list)*100)