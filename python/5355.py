t = int(input())

result = []
for _ in range(0, t) :
    input_data = input().split()

    num = float(input_data[0])
    for i in range(1, len(input_data)) :
        if (input_data[i] == "%") :
            num += 5
        if (input_data[i] == "@") :
            num *= 3
        if (input_data[i] == "#") :
            num -= 7
    result.append(num)

for res in result :
    print("{:.2f}".format(res))