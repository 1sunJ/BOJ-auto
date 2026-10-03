import math

def solution(brown, yellow):
    total = brown + yellow

    divisors = []
    for i in range(1, int(math.sqrt(total)) + 1) :
        if total % i == 0 :
            divisors.append(i)
    
    for c in divisors :
        r = total // c
        if (c - 2) * (r - 2) == yellow :
            return (r, c)
