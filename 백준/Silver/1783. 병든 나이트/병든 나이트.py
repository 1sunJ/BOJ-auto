import math

N, M = map(int, input().split())

if N >= 3 :
    if M >= 7 :
        print(M-2)
    elif M >= 4 :
        print(4)
    else :
        print(M)
elif N == 2 :
    if M >= 7 :
        print(4)
    else :
        print(math.ceil(M/2))
else : # N == 1
    print(1)