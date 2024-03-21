import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

answer = 0
for i in range(N) :
    answer += arr[i-1][0] * arr[i][1]
    answer -= arr[i][0] * arr[i-1][1]

print(round(abs(answer) / 2, 1))