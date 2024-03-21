import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

arr.sort()
answer1 = abs(sum(arr[:3:]))
answer2 = [0, 1, 2]

for i in range(N) :
    l, r = i + 1, N - 1
    while l < r :
        summ = arr[i] + arr[l] + arr[r]
        if answer1 > abs(summ) :
            answer1 = abs(summ)
            answer2 = [i, l, r]

        if summ > 0 :
            r -= 1
        elif summ < 0 :
            l += 1
        else :
            break

for i in sorted(answer2) :
    print(arr[i], end = ' ')