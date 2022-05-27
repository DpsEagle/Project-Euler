from time import time
from Problem22Names import NameList


t = time()
NameList.sort()

def AlphabeticalValue(Position):
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
          "w", "x", "y", "z"]
    Value=0
    LowerName = Position.lower()
    for x in LowerName:
        if x in alphabet:
            ValueToAdd=alphabet.index(x)
            Value+=ValueToAdd+1
    return Value

TotalNameScore=0

for x in NameList:
    print(x)
    NameScore=AlphabeticalValue(x)
    print(NameScore)
    RealNameScore=NameScore * (NameList.index(x) + 1)
    TotalNameScore+=RealNameScore
print(TotalNameScore)

tt = time()-t
print("Time to complete is",tt)