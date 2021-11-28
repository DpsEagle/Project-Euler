product=0
array=[]
def isPalindrome(product):
    s=str(product)
    return s==s[::-1]
            
for i in range(100,1000):
    for x in range(100,1000):
            product=i*x
            ans=isPalindrome(product)
            if ans:
                array.append(product)


big=max(array)
print(big)
            






        
    

            
        
