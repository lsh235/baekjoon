A, B = map(int, input().split())

count = 1
stop=True
while True:
    if A == B :
        print(count)
        break

    if B == 0 or A > B:
        print(-1)
        break
    elif B % 2 == 0 :
        B = B // 2
        count += 1
    elif B % 10 == 1:
        B = B // 10
        count += 1
    else :
        if stop == False :
            print(-1)
            break
        stop = False