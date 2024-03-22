N = int(input())
arr = list(map(int, input().split()))

arr2 = []
answer = {}
for i in range(N) :
    arr2.append([i, arr[i]])
    answer[arr[i]] = 0

arr2.sort(key=lambda x : x[1])
maxV = arr2[-1][1]

for i in range(N) :
    idx, value = arr2[i]
    for j in range(value*2, maxV+1, value) :
        if not j in answer :
            continue

        answer[value] += 1
        answer[j] -= 1

print(*answer.values())