repeat = int(input())

for _ in range(repeat) :
    r, e, c= (map(int, input().split()))
    ad_revenue = e - c
    if (r == ad_revenue) :
        print("does not matter")
    elif (r < ad_revenue) :
        print("advertise")
    elif (r > ad_revenue) :
        print("do not advertise")