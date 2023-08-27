start_time_hour, start_time_min, start_time_sec = map(int, input().split())
cooking_time_sec = int(input())

plus_hour, plus_min, plus_sec = 0, 0, 0
if (cooking_time_sec >= 3600) :
    plus_hour, cooking_time_sec = divmod(cooking_time_sec, 3600)

if (cooking_time_sec >= 60) :
    plus_min, plus_sec = divmod(cooking_time_sec, 60)
else :
    plus_sec = cooking_time_sec

start_time_hour += plus_hour
start_time_min += plus_min
start_time_sec += plus_sec

plus_hour, plus_min, plus_sec = 0, 0, 0
if (start_time_sec > 59) :
    plus_min, rem_sec = divmod(start_time_sec, 60)
    start_time_sec = rem_sec
    start_time_min += plus_min

if (start_time_min > 59) :
    plus_hour, rem_min = divmod(start_time_min, 60)
    start_time_min = rem_min
    start_time_hour += plus_hour

if (start_time_hour > 23) :
    _, rem_hour = divmod(start_time_hour, 24)
    start_time_hour = rem_hour

print(start_time_hour, start_time_min, start_time_sec)