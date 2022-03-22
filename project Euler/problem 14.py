from time import time
t = time()

def CollatzSequence(x):
    SequenceLength=0
    while x!=1:
        if x%2==0:
            n=x/2
            SequenceLength+=1
        else:
            n=3*x+1
            SequenceLength+=1
        x=n
    return(SequenceLength)

Largest=0
Num=0
for x in range(1,1000000):
    SequenceLength=CollatzSequence(x)
    if SequenceLength>Largest:
        Largest=SequenceLength
        num=x
        print(Largest)
        print(num)

print("Largest number is",num)
tt = time()-t
print(tt)
