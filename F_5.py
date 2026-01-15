"""
Task 
Write a function that takes age and returns:
"Child" if < 13
"Teen" if 13–19
"Adult" if ≥ 20
"""
def age():
    a=int(input("enter your age : "))
     
    if a<13:
        return "child "
    elif a>=13 and  a<=19:
        return "teen "
    else :
        return "adult"
results=age()
print(results)