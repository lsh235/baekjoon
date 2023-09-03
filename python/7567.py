dishs = list(input())

height = 10
dish = dishs[0]
for i in range(1, len(dishs)) :
    if (dish == dishs[i]) :
        height += 5
    else :
        height += 10
    dish = dishs[i]
print(height)