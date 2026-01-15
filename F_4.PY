"""
Write a function that takes a number and returns:

"Positive"

"Negative"

"Zero"

"""
def PNZ():
    a=int(input("enter the number  "))
     
    if a>0:
        return f"number is positive {a}"
    elif a<0:
        return f"number is negative {a}"
    else:
        return f"number is zero {a}"
    
results=PNZ()
print(results)


    