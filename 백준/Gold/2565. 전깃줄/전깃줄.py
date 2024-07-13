'''
ex1
[[1, 8], [2, 2], [3, 9], [4, 1], [6, 4], [7, 6], [9, 7], [10, 10]]
 => LIS

'''

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

arr.sort(key = lambda x : x[0])

dp = [1] * N #  dp[i] = idx 0 ~ i의 LIS

for i in range(1, N) :
    for j in range(i) :
        if arr[j][1] < arr[i][1] :
            dp[i] = max(dp[i], dp[j] + 1)

print(N - max(dp))