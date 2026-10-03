def solution(n):
    l, r = 1, 1
    total = 1
    answer = 0
    while l <= n :
        if total == n :
            answer += 1
            r += 1
            total += r          
        elif total > n :
            total -= l
            l += 1
        else :
            r += 1
            total += r
    
    return answer