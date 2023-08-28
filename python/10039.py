result = 0
for _ in range(5):
    jumsu = int(input())
    if jumsu < 40:
        result += 40
        continue
    result += jumsu

print(result//5)