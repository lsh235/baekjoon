repeat = int(input())

result_list = []
for _ in range(repeat) :
    num_list = list(map(int, input().split()))
    res = False 
    for i in num_list :
        dup = num_list.count(i)
        if dup == 3 :
            result_list.append(10000+(i*1000))
            res = True
            break
        if dup == 2 :
            result_list.append(1000+(i*100))
            res = True
            break

    if res == False :
        result_list.append(max(num_list)*100)
print(max(result_list))