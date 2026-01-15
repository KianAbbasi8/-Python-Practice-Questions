# Write a function that takes two numbers and returns the bigger one.

def find():
    a=int(input("enter the 1st number "))
    b=int(input("enter the 2nd number "))
    
    if a>b:
        return f"Greater number is 1st {a} : "
    elif b>a:
        return f"Greater number is 2nd {b} "

result=find()
print(result)