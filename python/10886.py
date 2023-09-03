repeat = int(input())

vote_list = []
for _ in range(repeat) :
    vote_list.append(int(input()))

print("Junhee is cute!") if vote_list.count(1) > vote_list.count(0) else print("Junhee is not cute!")