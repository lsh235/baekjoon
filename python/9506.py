import math

while True :
    measure_list = []
    num = int(input())
    if(num == -1) :
        break

    for i in range(1, int(math.sqrt(num) + 1)) :
        num_measure = int(num % i)
        if num_measure == 0 :
            measure_list.append(i)
            measure_list.append(num//i)
    measure_list.sort()
    measure_list = measure_list[:-1]
    if (sum(measure_list) == num) :
        str_list = [str(x) for x in measure_list]
        result = " + ".join(str_list)
        print(num, "=", result)
    else :
        print(num, "is NOT perfect.")