friend_list = []
while True :
    boy_firend, girl_firend = map(int, input().split())
    if (boy_firend == 0 and girl_firend == 0) :
        break
    friend_list.append(boy_firend + girl_firend)

for i in friend_list :
    print(i)