N = int(input())

M = 2 ** 32 - N

result = str(bin(N ^ M))

answer = 0
for x in result :
    if x == '1' :
        answer += 1

print(answer)