
n= int(input("enter number of rows"))
p=0
for i in range(n):
    for j in range(0,i+1):
        if p>25:
            p=0
        print(chr(p+65),end="")
        p=p+1
    print("")
