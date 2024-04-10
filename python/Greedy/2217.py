N = int(input())
lope = [int(input()) for _ in range(N)]

lope.sort()

total_w = []
for w in lope:
    total_w.append(w * N)
    N -= 1
print(max(total_w))