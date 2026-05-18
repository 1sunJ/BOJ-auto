def solution(n):
    n1, n2, n3 = 0, 1, 1
    for i in range(n - 2) :
        n1 = n2
        n2 = n3
        n3 = (n1 + n2) % 1234567
    
    return n3