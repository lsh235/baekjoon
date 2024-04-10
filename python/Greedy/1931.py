# 입력 받기
N = int(input())
meetings = []
for _ in range(N):
    start, end = map(int, input().split())
    meetings.append((start, end))

# 끝나는 시간을 기준으로 회의를 정렬
meetings.sort(key=lambda x: x[1])

# 회의 배정하기
count = 0
end_time = 0
for meeting in meetings:
    if meeting[0] >= end_time:  # 현재 회의의 시작 시간이 이전 회의의 끝나는 시간보다 뒤에 있을 때
        count += 1
        end_time = meeting[1]  # 현재 회의의 끝나는 시간으로 갱신

# 결과 출력
print(count)