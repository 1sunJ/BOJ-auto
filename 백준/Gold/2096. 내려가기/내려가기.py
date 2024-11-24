import sys
input = sys.stdin.readline

dp1 = [0, 0, 0] # maximum
dp2 = [0, 0, 0] # minimum

for _ in range(int(input())) :
    cur = list(map(int, input().split()))

    dp1 = [max(dp1[:2])+cur[0], max(dp1[:])+cur[1], max(dp1[1:])+cur[2]]
    dp2 = [min(dp2[:2])+cur[0], min(dp2[:])+cur[1], min(dp2[1:])+cur[2]]

print(max(dp1), min(dp2))