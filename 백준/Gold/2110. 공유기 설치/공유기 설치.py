import sys
input = sys.stdin.readline

def bs() :
    l, r = 1, arr[N-1] - arr[0]

    while l <= r :
        mid = (l + r) // 2 # interval
        # print("!!", mid, l, r)

        cnt = 1
        location = arr[0]

        for i in range(N) :
            if arr[i] - location >= mid :
                cnt += 1
                location = arr[i]
        
        if cnt >= C :
            global answer
            answer = mid
            l = mid + 1
        else :
            r = mid - 1


N, C = map(int, input().split())
arr = [int(input()) for _ in range(N)]

arr.sort()

answer = 0
bs()

print(answer)