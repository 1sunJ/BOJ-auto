import math

def makePrimes(n) :
    
    arr = [True] * (n+1)
    primes = []

    for i in range(2, n+1) :
        if arr[i] :
            primes.append(i)

            for j in range(i*2, n+1, i) :
                arr[j] = False

    return primes

N = int(input())
if N == 1 :
    print(0)
    exit()

primes = makePrimes(N)

answer = 0
l, r, cntSum = 0, 0, primes[0]
c = 0
while l <= r and primes[l] <= N // 2 :
    if cntSum == N :
        answer += 1
        cntSum -= primes[l]
        l += 1
    elif cntSum < N and r < len(primes) - 1 :
        r += 1
        cntSum += primes[r]
    else :
        cntSum -= primes[l]
        l += 1

isPrime = True
for i in range(2, int(math.sqrt(N)) + 1) :
    if N % i == 0 :
        isPrime = False
        break
if isPrime :
    answer += 1

print(answer)