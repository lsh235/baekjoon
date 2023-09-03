pen_str = input()

pen_str_middle = int(len(pen_str)/2)
pen_str_front = []
pen_str_back = []
if (len(pen_str)%2 != 0) :
    pen_str_front = pen_str[:pen_str_middle]
    pen_str_back = pen_str[pen_str_middle+1:]
else :
    pen_str_front = pen_str[:pen_str_middle]
    pen_str_back = pen_str[pen_str_middle:]

pen_str_back = pen_str_back[::-1]
if pen_str_front == pen_str_back :
    print(1)
else :
    print(0)