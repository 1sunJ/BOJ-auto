import sys

input = sys.stdin.readline

N, H = map(int, input().split())

top = [0] * (H + 1)
bottom = [0] * (H + 1)
for i in range(N // 2) :
    top[int(input())] += 1
    bottom[int(input())] += 1

for i in range(H - 1, 0, -1) :
    top[i] += top[i + 1]
    bottom[i] += bottom[i + 1]

top = top[1::]
bottom = bottom[1::][::-1]

result = [top[i] + bottom[i] for i in range(H)]
answer1 = min(result)
answer2 = result.count(answer1)
print(answer1, answer2)