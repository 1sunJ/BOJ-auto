import sys

input = sys.stdin.readline

N, K = map(int, input().split())
arr = [len(input().rstrip()) for _ in range(N)] + [-1] * (K + 1)
count = [0] * 22

answer = 0
for i in range(N) :
    old = arr[i - K - 1]
    count[old] -= 1

    new = arr[i]
    answer += count[new]
    count[new] += 1

print(answer)