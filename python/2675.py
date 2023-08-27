t = int(input())

result = []
for _ in range(0, t) :
    S = input().split()

    result_s = ""
    for s in list(S[1]) :
        result_s += str(s) * int(S[0])
    result.append(result_s)

for s in result :
    print(s)