from collections import Counter

first_list = []
second_list = []

for _ in range(3) :
    first, second = map(int, input().split())
    first_list.append(first)
    second_list.append(second)

first_list = Counter(first_list)
second_list = Counter(second_list)

first_result = [key for key, value in first_list.items() if value == 1]
second_result = [key for key, value in second_list.items() if value == 1]

print(first_result[0], second_result[0])