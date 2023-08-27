start_time_hour, start_time_min = map(int, input().split())
cooking_time_min = int(input())

start_time_min += cooking_time_min

if (start_time_min > 59) :
    plus_hour, rem_min = divmod(start_time_min, 60)
    start_time_min = rem_min
    start_time_hour += plus_hour
    if (start_time_hour > 23) :
        _, rem_hour = divmod(start_time_hour, 24)
        start_time_hour = rem_hour

print(start_time_hour, start_time_min)