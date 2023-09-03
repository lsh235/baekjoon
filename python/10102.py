from collections import Counter

num = int(input())
vote_list = list(input())

vote_count_list = Counter(vote_list)

if (vote_count_list["A"] == vote_count_list["B"]) :
    print("Tie")
elif(vote_count_list["A"] > vote_count_list["B"]) :
    print("A")
elif(vote_count_list["A"] < vote_count_list["B"]) :
    print("B")

# or
# vote_list = input()
# print("Tie") if vote_list.count("A") == vote_list.count("B") else print("A") if vote_list.count("A") > vote_list.count("B") else print("B")