import sys
from collections import deque

T = int(input())

for _ in range(T) :
    opers = input().rstrip()
    n = int(input())
    deq = deque(input()[1:-1:].split(','))
    if deq[0] == '' :
        deq = deque([])
    
    p = 1 # 1 -> left / -1 -> right
    isError = False
    for o in opers :
        if o == 'R' :
            p *= -1
        else :
            if not deq :
                isError = True
                break
            
            if p == 1 :
                deq.popleft()
            else :
                deq.pop()
    
    if isError :
        print("error")
        continue

    deq = list(deq)
    if p == -1 :
        deq = deq[::-1]
        
    print("[", end = '')
    print(*deq, sep =',', end = '')
    print("]")