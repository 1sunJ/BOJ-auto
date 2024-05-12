import sys

def recur(a, b, c) :
    if dp[a][b][c] != INF :
        return dp[a][b][c]
    if a <= 0 or b <= 0 or c <= 0 :
        dp[a][b][c] = 1
        return 1
    elif a > 20  or b > 20 or  c > 20 :
        dp[a][b][c] = recur(20, 20, 20)
        return recur(20, 20, 20)
    elif a < b and b < c :
        dp[a][b][c] = recur(a, b, c-1) + recur(a, b-1, c-1) - recur(a, b-1, c)
        return recur(a, b, c-1) + recur(a, b-1, c-1) - recur(a, b-1, c)
    else :
        dp[a][b][c] = recur(a-1, b, c) + recur(a-1, b-1, c) + recur(a-1, b, c-1) - recur(a-1, b-1, c-1)
        return recur(a-1, b, c) + recur(a-1, b-1, c) + recur(a-1, b, c-1) - recur(a-1, b-1, c-1)
    
INF = -sys.maxsize
dp = [[[INF] * 101 for _ in range(101)] for _ in range(101)]

while True :
    a, b, c = map(int, input().split())
    if a == -1 and b == -1 and c == -1 :
        break

    print("w(%d, %d, %d) = %d" %(a, b, c, recur(a, b, c)))