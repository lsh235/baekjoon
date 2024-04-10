N, K = map(int, input().split())
money = []
for _ in range(N):
    tmp_m = int(input())
    if tmp_m > K:
        continue
    money.append(tmp_m)

money.sort(reverse=True)

count = 0
for m in money:
    if K // m > 0:
        tmp = K // m
        count += tmp
        K -= tmp * m

print(count)