import math


def Factors(x):
    ListOfFactors=[]
    for i in range(1, int(math.sqrt(x) + 1)):
        if x%i==0:
            ListOfFactors.append(i)
            if i!=1 and i*i!=x:
                ListOfFactors.append(x/i)
    return ListOfFactors



def AbundantNumbersUpTo():
    ListOfAbundantNumbers=[]
    for i in range (1,28112):
        ListOfFactors=Factors(i)
        total=0
        for x in ListOfFactors:
            total+=x
            if total>i:
                ListOfAbundantNumbers.append(i)
    return ListOfAbundantNumbers



AbundantNumList=AbundantNumbersUpTo()
Total=0

for x in range(1,3):
    for i in AbundantNumList:
        for j in AbundantNumList:
            if i>x:
                Total+=x
                print(Total)
                break
            elif j>x:
                Total+=x
                print(Total)
                break
            elif i+j==x:
                pass




