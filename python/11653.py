import math

num = int(input())
i = math.sqrt(num)

k = 2
while k <= i:
    quo, rem = divmod(num, k)
    if (rem == 0) :
        print(k)
        num = num // k
    else :
        k += 1

if (num > 1) :
    print(num)