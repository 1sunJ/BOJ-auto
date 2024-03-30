def dfs(idx) :
    if idx == N :
        global answer
        answer += 1
        return
    
    # idx 행 / i 열
    for i in range(N) :
        if i in s :
            continue

        check = False
        for j in range(idx) :
            if abs(j-idx) == abs(arr[j]-i) :
                check = True
        if check : 
            continue

        arr[idx] = i
        s.add(i)
        dfs(idx+1)
        s.remove(i)
        
N = int(input())

arr = [False] * N
answer = 0
s = set()

dfs(0)
print(answer)