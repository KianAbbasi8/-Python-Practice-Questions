set_1=set()
set_2=set()

print("enter the 5 elements of 1st set  : ")
for i in range(5):
    n1= int(input(f"enter the {1+i} "))
    set_1.add(n1)
print("enter element of 2nd set : ")
for i in range(5):
    n2=int(input(f"enter element : {1+i} "))
    set_2.add(n2)
print("out put ")
print(f"first set is  : {set_1}")
print(f"2nd set is : {set_2}")
print(f"union is : {set_1|set_2}")
print(f"inter section is : {set_1 & set_2}")
 
