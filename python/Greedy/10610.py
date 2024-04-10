from collections import Counter

n = input()
digist = list(str(n))

digist_num = sum(int(d) for d in digist)
remainder_3 = digist_num % 3

num_counter = Counter(digist)
has_zero = '0' in num_counter

if remainder_3 == 0 and has_zero:
    sorted_digits = sorted(digist, reverse=True)
    print(int(''.join(sorted_digits)))
else:
    print(-1)