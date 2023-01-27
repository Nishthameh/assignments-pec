size=0
list1=[]
list2=[]
list3=[]
list4=[]
while (size<10):
    value=int(input("enter value"))
    if value>0:
        list1.append(value)
        if value%2==0:
            list3.append(value)
        else:
            list4.append(value)
    elif value<0:
        list2.append(value)
        if value%2==0:
            list3.append(value)
        else:
            list4.append(value)
    size+=1
print(list1)
print(list2)
print(list3)
print(list4)
def cont(list):
    count={}
    for i in list:
        if i in count:
            count[i]+=1
        else:
            count[i]=1
    return count

print(cont(list1))
print(cont(list2))
print(cont(list3))
print(cont(list4))

