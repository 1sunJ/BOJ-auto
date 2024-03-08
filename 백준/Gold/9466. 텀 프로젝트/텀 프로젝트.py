import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

# code 2 : python3 pass / pypy3 memory exceeded
def dfs(idx) :
    if done[idx] == -1 or done[idx] == 2 :  # 2 : cycle check complete / -1 : visited
        return
    
    done[idx] += 1
    dfs(arr[idx])
    
    if done[idx] == 1 :
        done[idx] = -1
    
for _ in range(int(input())) :
    N = int(input())
    arr = [0] + list(map(int, input().split()))
    
    done = [0] * (N+1)  # 0 : no visit / 1 : visit but fail / 2, 3 : team

    for i in range(1, N+1) :    # O(N)
        if done[i] : continue
        dfs(i)

    ans = 0
    for i in range(1, N+1) :
        if done[i] != 2 :
            ans += 1

    print(ans)