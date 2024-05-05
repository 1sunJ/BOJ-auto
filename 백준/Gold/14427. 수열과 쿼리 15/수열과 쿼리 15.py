import sys
import heapq
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
M = int(input())

arr2 = [-1] + arr[::]
for i in range(N) :
    arr[i] = [arr[i], i+1]
heapq.heapify(arr)

for _ in range(M) :
    inp = input()

    # arr의 갱신(삭제) 작업은 else에서
    if inp[0] == '1' :
        q, i, v = map(int, inp.split())
        arr2[i] = v
        heapq.heappush(arr, [v, i])

    else :
        while True :
            minV, minI = arr[0]
            if arr2[minI] == minV :
                print(minI)
                # print("output :", minI)
                break

            heapq.heappop(arr)
            heapq.heappush(arr, [arr2[minI], minI])