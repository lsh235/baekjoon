result = int(input())

sum = 0
i = 1
count = 0
while True :
    sum += i
    count += 1
    if sum > result :
        count -= 1
        break
    i += 1
print(count)