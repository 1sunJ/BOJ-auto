def isPalindrome(n) :
    n = list(str(n))

    if n == n[::-1] :
        return True
    else :
        return False
    
def makePrimes(n) :
    isPrimeArr = [True] * (n+1)
    primes = []

    for i in range(2, n+1) :
        if isPrimeArr[i] :
            primes.append(i)

            for j in range(i*2, n+1, i) :
                isPrimeArr[j] = False

    return primes

a, b = map(int, input().split())

primes = makePrimes(min(b, 10000000))

for x in primes :
    if x >= a and isPalindrome(x) :
        print(x)

print(-1)