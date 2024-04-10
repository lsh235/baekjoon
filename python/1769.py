x = input()
count = 0

while len(x) >= 2:
    digits_sum = sum(int(digit) for digit in x)
    x = str(digits_sum)
    count += 1

if int(x) % 3 == 0:
    print(count)
    print("YES")
else:
    print(count)
    print("NO")