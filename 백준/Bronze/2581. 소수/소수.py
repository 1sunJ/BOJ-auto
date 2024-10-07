def isPrime(n) :
    for i in range(2, int(n ** (1/2) + 1)) :
        if n % i == 0 :
            return False
    return True

A = int(input())
B = int(input())

if A == 1 :
    A = 2

minPrime = 0
primeSum = 0
for i in range(A, B + 1) :
    if isPrime(i) :
        if not minPrime :
            minPrime = i
        primeSum += i

if not minPrime :
    print(-1)
else :
    print(primeSum)
    print(minPrime)