square = 38
n = int(input())

answer = 0
while n :
    if 2 ** square <= n :
        answer += 3 ** square
        n -= 2 ** square
    
    square -= 1

print(answer)