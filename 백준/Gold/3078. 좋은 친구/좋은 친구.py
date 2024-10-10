import sys

input = sys.stdin.readline

N, K = map(int, input().split())
arr = [-1] * K + [len(input()) for _ in range(N)]

l, r = 0, K
map = {arr[K] : 1, -1 : -1}

answer = 0
for i in range(K + 1, N + K) :
    # 탈락
    old = arr[i - K - 1]
    map[old] -= 1

    # 추가
    new = arr[i]
    if new in map :
        answer += map[new]
        map[new] += 1
    else :
        map[new] = 1

print(answer)