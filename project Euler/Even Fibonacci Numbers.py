total = 0
x=1
y=1
z=0

while total<4000000:



    z=x+y
    if z%2==0:
        total+=z
    x=z+y
    if x%2==0:
        total+=x
    y=z+x
    if y%2==0:
        total+=x

print(total)
        
    
    
    
