import sys
input = sys.stdin.readline

def search(n) :
    l, r = 0, len(result) - 1

    while l < r :
        mid = (l + r) // 2
        midValue = result[mid]

        if n <= midValue :
            r = mid
        else :
            l = mid + 1

    return r

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

arr.sort()

result = [arr[0][1]]
result2 = [[0]]
for i in range(1, N) :
    n = arr[i][1]

    if n > result[-1] :
        result.append(n)
        result2.append([i])
    else :
        p = search(n)
        result[p] = n
        result2[p].append(i)

result3 = [0] * (len(result) - 1) + [result2[-1][-1]]
for i in range(len(result)-2, -1, -1) :
    for j in range(len(result2[i]) - 1, -1, -1) :
        if result2[i][j] < result3[i + 1] :
            result3[i] = result2[i][j]
            break

answer = set(range(N))
for x in result3 :
    answer.discard(x)


print(len(answer))
for i in answer :
    print(arr[i][0])