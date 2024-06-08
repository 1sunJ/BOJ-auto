from sys import maxsize

def dfs(i, ar) :
    if i == N :
        global answer
        answer = min(answer, calculate(ar))
        return
    
    dfs(i+1, ar)
    dfs(i+1, ar + [i])

def calculate(ar) :
    tmpCounts = counts[::]
    
    price = 0
    for i in ar :
        for c in arr[i][1] :
            tmpCounts[ord(c) - ord('A')] -= 1
        price += arr[i][0]

    for x in tmpCounts :
        if x > 0 :
            return maxsize
    return price

T = input()
N = int(input())
arr = []
for _ in range(N) :
    price, name = input().split()
    arr.append([int(price), sorted(name)])

counts = [0] * 26
for c in T :
    counts[ord(c) - ord('A')] += 1

answer = maxsize
dfs(0, [])
print(-1 if answer == maxsize else answer)