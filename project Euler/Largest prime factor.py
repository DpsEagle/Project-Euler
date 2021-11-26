number=600851475143
Factors=[]
PrimeFactors=[]

for x in range(1,number):
    if number%x==0:
        Factors.append(x)

  
for i in Factors:
    for y in range(2,i):
        if i%y==0:
            PrimeFactors.append(i)


for element in PrimeFactors:
    if element in Factors:
        Factors.remove(element)


x=max(Factors)
print(x)

