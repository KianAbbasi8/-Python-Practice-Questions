li=[]
for i in range(5):
    marks=int(input(f"enter the marks of student {1+i} "))
    li.append(marks)
    li.sort()
print(li)