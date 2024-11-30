INPUT_ABS_MAX = 1000001
MODULO = 1000000000

n = int(input())

dp = [-1] * INPUT_ABS_MAX
dp[0] = 0
dp[1] = 1

for i in range(2, abs(n) + 1) :
    dp[i] = (dp[i-2] + dp[i-1]) % MODULO

if n == 0 :
    print(0)
    print(0)
elif n < 0 and n % 2 == 0 :
    print(-1)
    print(dp[abs(n)])
else :
    print(1)
    print(dp[abs(n)])