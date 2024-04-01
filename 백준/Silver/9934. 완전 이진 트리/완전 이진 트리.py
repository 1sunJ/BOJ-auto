def go(l, r, d) :
    if l > r :
        return 
    
    mid = (l + r) // 2
    tree[d].append(arr[mid])

    go(l, mid - 1, d + 1)
    go(mid + 1, r, d + 1)


K = int(input())
arr = list(map(int, input().split()))

tree = [[] for _ in range(K)]
go(0, len(arr) - 1, 0)

for x in tree :
    print(*x)