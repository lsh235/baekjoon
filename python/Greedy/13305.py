N = int(input())
km = list(map(int, input().split()))
city = list(map(int, input().split()))

total_pay = 0
cheap_price = city[0]
for i in range(N-1):
    if cheap_price > city[i]:
        cheap_price = city[i]
    total_pay += cheap_price * km[i]
print(total_pay)