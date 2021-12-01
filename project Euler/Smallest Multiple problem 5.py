Divisible = False
num=1

while not Divisible:
    for x in range(1,20):
        if num%x!=0:
            num+=1
            Divisible=False
        else:
            num=num
            Divislbe=True
            print(num)
            
          
if Divisible:
    print(num)
    
