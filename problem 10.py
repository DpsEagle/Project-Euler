def isPrime(num):
    for x in range(2,int(num**0.5)+1):
        if num%x==0:
            return False
    return True


total=0
for i in range(2,2000000):
    if isPrime(i):
        total+=i
print(total)
