import sys
input = sys.stdin.readline

N = int(input())
strs = [input().rstrip() for _ in range(N)]
answer = dict()

for s in strs :
    extension = s.split('.')[1]

    if extension in answer :
        answer[extension] += 1
    else :
        answer[extension] = 1

extensions = sorted(list(answer.keys()))

for extension in extensions :
    print(extension, answer[extension])