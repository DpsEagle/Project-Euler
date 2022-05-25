def Factorial(x):
    total=1
    for i in range(x,0, -1):
        total= total*i
    return total

Number=str(Factorial(100))
total=0
for x in Number:
    total+=int(x)

print(total)







