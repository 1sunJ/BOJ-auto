def bs(lenn) :
    l, r = 0, lenn - 1

    p = r
    while l < r :
        mid = (l+r) // 2
        midValue = answer[mid]

        if arr[i] <= midValue :
            p = mid
            r = mid
        else :
            l = mid + 1

    return p

N = int(input())
arr = list(map(int, input().split()))

answer = [arr[0]]

for i in range(1, N) :
    if arr[i] > answer[len(answer)-1]  :
        answer.append(arr[i])
    else :
        # 여기서 이분탐색! arr[i] <= answer[j] 탐색을 선형이 아닌 BS로
        p = bs(len(answer))
        answer[p] = arr[i]
    # print("!!", answer)
    
print(len(answer))