import heapq
import sys
input = sys.stdin.readline

N = int(input())
arr = [int(input()) for _ in range(N)]

heapq.heapify(arr)

ans = 0
for i in range(N-1) :
    a = heapq.heappop(arr)
    b = heapq.heappop(arr)
    ans += a+b

    heapq.heappush(arr, a+b)

print(ans)