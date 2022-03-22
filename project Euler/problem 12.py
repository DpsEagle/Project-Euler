from time import time
t = time()

def factors(x):
    NumberOfFactors=0
    for i in range(1,int(x**0.5)):
        if x%i==0:
            NumberOfFactors+=1
    return NumberOfFactors

found=False
Difference=1
Number=0
while found==False:
    Number+=Difference
    Difference+=1
    FactorsOfNum=factors(Number)
    if FactorsOfNum>=250:
        print("The number is:",Number)
        break

tt = time()-t
print(tt)
