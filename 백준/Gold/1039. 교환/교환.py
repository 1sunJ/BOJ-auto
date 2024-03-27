from collections import deque

N, K = map(int, input().split())
l = len(str(N))

visited = set()
visited.add((str(N), 0))
que = deque([])
que.append((str(N), 0))

answer = 0
while que :
    n, k = que.popleft()

    if k == K :
        answer = max(answer, int(n))
        continue

    numbers = list(n)

    for i in range(l) :
        for j in range(i + 1, l) :
            if i == 0 and numbers[j] == '0' :
                continue

            numbers[i], numbers[j] = numbers[j], numbers[i]
            nn = ''.join(numbers)
            if (nn, k + 1) not in visited :
                que.append((nn, k + 1))
                visited.add((nn, k + 1))
            
            numbers[i], numbers[j] = numbers[j], numbers[i]

print(answer if answer else -1)