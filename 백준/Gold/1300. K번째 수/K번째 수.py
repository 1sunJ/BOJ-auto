def bs() :
    l, r = 0, k
    answer = 0

    # t = 0
    while l <= r :
        mid = (l + r) // 2

        cnt = 0
        for i in range(1, N+1) :
            cnt += min(mid // i, N)
        # print("!!", l, r, mid, cnt)

        if cnt < k :
            l = mid + 1
        else :
            r = mid - 1
            answer = mid
        
        # t += 1
        # if t == 400 : break
    
    return answer

N = int(input())
k = int(input())

print(bs())