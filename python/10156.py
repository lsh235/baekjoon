num_list = list(map(int, input().split()))

res = (num_list[0] * num_list[1]) - num_list[2]
if res > 0 :
    print(res)
else :
    print(0)