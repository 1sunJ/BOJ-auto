N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

arr.sort(key=lambda x : x[1], reverse=True)
days = [0] * (1001)

for day, score in arr :
    for j in range(day, 0, -1) :
        if not days[j] :
            days[j] = score
            break

print(sum(days))