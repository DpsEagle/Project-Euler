

def isPrime(num):

    for x in range(2, int(num**0.5) + 1):
        if x % i == 0:
            return False
    return True


def nthPrime(n):
    numberOfPrimes = 0
    prime = 1

    while numberOfPrimes < n:
        prime += 1
        if isPrime(prime):
            numberOfPrimes += 1
    return prime

print(nthPrime(10001))
