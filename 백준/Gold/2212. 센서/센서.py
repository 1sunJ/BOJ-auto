N = int(input())
K = int(input())
arr = list(map(int, input().split()))

arr.sort()
arr2 = [arr[i+1] - arr[i] for i in range(N - 1)]

arr2.sort()
print(sum(arr2[:N-K:]))