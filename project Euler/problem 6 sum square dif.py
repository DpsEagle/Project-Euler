SumOfX=0
XSquared=0
XSquared1=0


for x in range(1,101):
    SumOfX+=x
    XSquared=x**2
    XSquared1+=XSquared

SumOfXSquared=SumOfX **2   
dif=SumOfXSquared-XSquared1
print(dif)
    
