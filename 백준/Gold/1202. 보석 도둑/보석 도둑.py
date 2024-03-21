from heapq import *
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
W = [int(input()) for _ in range(K)]

arr.sort(key=lambda x : x[0], reverse = True)
W.sort()

heap = []
answer = 0

for w in W :
    while arr and arr[-1][0] <= w :
        heappush(heap, -arr.pop()[1])

    if not heap :
        continue

    answer -= heappop(heap)

print(answer)