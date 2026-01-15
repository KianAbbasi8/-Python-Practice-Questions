"""Write a function that returns the sum of numbers from 1 to N."""

def sum():
    a=int(input("enter the number  "))
    sum1=0
    for i in range(1,a+1):
        sum1=sum1+i
    
    
    
    return sum1
result=sum()
print(result)