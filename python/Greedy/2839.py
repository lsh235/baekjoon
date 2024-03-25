n = int(input())
count = 0

# 방법 1
if n % 5 == 0:                  # 5로 전부 나눠질 경우
    print(n//5)
else:
    while n > 0 :               # 안나눠질때
        n -= 3                  # 3으로 한번 빼보고
        count += 1
        if n % 5 == 0:          # 5로 나눠지는지 확인
            print(count + n//5) # 나눠지면 3,5 조합이므로 출력
            break
    else:
        print(-1)               # 3, 5 조합 어떤 수로 써도 안될때

# 방법 2
while n > 0:
    if n % 5 == 0:              # 5로 전부 나눠질 경우
        print(count + n//5)
        break
    n -= 3                      # 5로 전부 안나눠지면 3빼고 다시 5로 나눠보기 반복
    count += 1
else:
    print(-1)                   # 3, 5 조합 어떤 수로 써도 안될때