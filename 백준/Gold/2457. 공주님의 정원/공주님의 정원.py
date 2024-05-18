import sys
input = sys.stdin.readline

DAYS = (0, 0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365)

N = int(input())
INPUT = [list(map(int, input().split())) for _ in range(N)]

arr = []
for sm, sd, em, ed in INPUT :
    arr.append([DAYS[sm] + sd, DAYS[em] + ed])

arr.sort()

e = DAYS[3] + 1
i = 0
answer = 0
while i < N and e <= DAYS[12] :
    # e보다 작거나 같은 startDate를 가진 꽃들 중
    # endDate가 가장 큰 꽃 찾기
    tmp = e
    noFlower = True
    while i < N and arr[i][0] <= tmp :
        e = max(e, arr[i][1])
        i += 1
        noFlower = False
    
    if noFlower :
        e = -1
        break

    answer += 1

if e <= DAYS[12] :
    print(0)
else :
    print(answer)