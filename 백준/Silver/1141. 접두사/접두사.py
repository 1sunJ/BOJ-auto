N = int(input())
arr = [input() for _ in range(N)]

arr.sort()

answer = N
for i in range(N) : 
    for j in range(i+1, N) :
        if arr[j].startswith(arr[i]) :
            answer -= 1
            break

print(answer)