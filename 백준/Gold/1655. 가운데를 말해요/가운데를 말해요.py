import sys
import heapq

input = sys.stdin.readline

N = int(input())

maxHeap = []
minHeap = []

for _ in range(N) :
    n = int(input())

    if not maxHeap or -maxHeap[0] > n :
        heapq.heappush(maxHeap, -n)
    else :
        heapq.heappush(minHeap, n)

    if len(maxHeap) > len(minHeap) + 1 :
        heapq.heappush(minHeap, -heapq.heappop(maxHeap))
    elif len(maxHeap) < len(minHeap) :
        heapq.heappush(maxHeap, -heapq.heappop(minHeap))

    print(-maxHeap[0])