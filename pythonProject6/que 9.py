str= input("enter line of string")
str=str.split()
i=0
list2=[]
for i in str:
    if i not in list2:
        list2.append(i)
        if i in list2:
            print(i,";" ,str.count(i))
