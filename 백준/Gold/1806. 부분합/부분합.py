import sys
input = sys.stdin.readline

N, S = map(int, input().split())
arr = list(map(int, input().split()))

cumArr = arr.copy()
for i in range(1, N) :
    cumArr[i] += cumArr[i-1]

minLen = 0

l, r = 0, 0
while r < N :
    if l > r :
        r += 1
        continue

    if l == 0 :
        sum = cumArr[r]
    else :
        sum = cumArr[r] - cumArr[l-1]
    if sum >= S :
        if minLen == 0 :
            minLen = r-l+1
        else :
            minLen = min(minLen, r-l+1)
        l += 1
    else :
        r += 1

print(minLen)