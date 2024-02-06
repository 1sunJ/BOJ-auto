def isGood(i) :

    l, r = 0, N - 1
    if i == l :
        l += 1
    if i == r :
        r -= 1

    while l < r :
        summ = arr[r] + arr[l]

        if arr[i] < summ :
            r -= 1
            if i == r :
                r -= 1
        elif arr[i] > summ :
            l += 1
            if i == l :
                l += 1
        else :
            return True

    return False


N = int(input())
arr = list(map(int, input().split()))

arr.sort()

answer = 0
for i in range(N) :
    if isGood(i) :
        answer += 1

print(answer)