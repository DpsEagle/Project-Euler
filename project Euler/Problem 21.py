import math
from time import time
t = time()


def Factors(x):
    ListOfFactors=[]
    for i in range(1,int(math.sqrt(x))+1):
        if x%i==0:
            ListOfFactors.append(i)
            if i!=1 and i*i!=x:
                ListOfFactors.append(x/i)

    return ListOfFactors
print(Factors(15))

def FactorSum(List):
    total=0
    for x in List:
        total+=x
    return total

RealTotal=0


for x in range(200,10000):
    ListOfFactorsOfX=Factors(x)
    FirstTotal=FactorSum(ListOfFactorsOfX)
    print(x)
    for y in range(200,10000):
        ListOfFactorsOfY = Factors(y)
        SecondTotal = FactorSum(ListOfFactorsOfY)
        #print(SecondTotal)
        if x != y:
            if FirstTotal==y:
                if SecondTotal==x:
                    RealTotal+=FirstTotal
                    RealTotal+=SecondTotal

print("REAL TOTAL IS:,",RealTotal/2)
tt = time()-t
print(tt)