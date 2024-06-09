def dfs(idx, s, b) :
    if idx == N :
        global answer
        if not (s == 1 and b == 0) :
            answer = min(answer, abs(s-b))
        return

    dfs(idx+1, arr[idx][0] * s, arr[idx][1] + b) 
    dfs(idx+1, s, b) 
    
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

answer = 999999999999999
dfs(0, 1, 0)
print(answer)