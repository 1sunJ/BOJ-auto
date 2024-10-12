def isCycle(idx, ar) :
    visited[idx]
    next = arr[idx]
    if next == ar[0] :
        global answer
        answer += ar
        for x in ar :
            visited[x] = True
        return
    
    if not visited[next] and not next in ar :
        isCycle(next, ar + [next])

N = int(input())
arr = [0] + [int(input()) for _ in range(N)]

visited = [False] * (N + 1)
answer = []

for i in range(1, N + 1) :
    if i == arr[i] :
        answer.append(i)
        continue

    if visited[i] :
        continue

    isCycle(i, [i])

print(len(answer), *sorted(answer), sep = '\n')