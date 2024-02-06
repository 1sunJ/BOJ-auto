import heapq
import sys
input = sys.stdin.readline

for _ in range(int(input())) :
    k = int(input())

    hq1 = [] # maxHeap
    hq2 = [] # minHeap
    s = {}
    l = 0
    for _ in range(k) :
        c, n = input().split()
        n = int(n)

        if c == 'I' :
            heapq.heappush(hq1, -n)
            heapq.heappush(hq2, n)
            if n in s :
                s[n] += 1
            else :
                s[n] = 1
            l += 1

        else :
            if not l :
                continue
            l -= 1

            if n == 1 :
                while True :
                    popValue = -heapq.heappop(hq1)
                    if popValue in s and s[popValue] > 0 :
                        break

                s[popValue] -= 1

            else :
                while True :
                    popValue = heapq.heappop(hq2)
                    if popValue in s and s[popValue] > 0 :
                        break

                s[popValue] -= 1

        # print("hq1", hq1)
        # print("hq2", hq2)
        # print("set", s)

    if l :
        while True :
            maxV = -heapq.heappop(hq1)
            if s[maxV] > 0 :
                break
        
        while True :
            minV = heapq.heappop(hq2)
            if s[minV] > 0 :
                break

        print(maxV, minV)
    else :
        print("EMPTY")