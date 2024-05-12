import heapq

N = int(input())
if N == 1 :
    input()
    print(0)
    exit()

my = int(input())
arr = [-int(input()) for _ in range(N-1)]

heapq.heapify(arr)


answer = 0
while True :
    maxx = -heapq.heappop(arr)

    if my > maxx :
        break

    my += 1
    answer += 1
    heapq.heappush(arr, -(maxx - 1))

print(answer)