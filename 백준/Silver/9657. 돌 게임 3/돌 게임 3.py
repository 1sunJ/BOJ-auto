N = int(input())

result = [-1, 0, 1, 0, 0, 0] + [-1] * (N - 5)

for i in range(6, N + 1) :
    if result[i - 1] or result[i - 3] or result[i - 4] :
        result[i] = 0
    else :
        result[i] = 1

print(("SK", "CY")[result[N] % 2])