from collections import deque

N, L = map(int, input().split())
arr = list(map(int, input().split()))

# (value, idx)
dq = deque([(10 ** 9 + 1, -1)])
answer = [0] * (N)

for i in range(N) :

    while dq and (dq[-1][0] > arr[i]) :
        dq.pop()

    dq.append((arr[i], i))

    while dq[0][1] <= i - L :
        dq.popleft()
    
    answer[i] = dq[0][0]

print(*answer)