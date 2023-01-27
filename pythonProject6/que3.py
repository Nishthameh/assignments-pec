import math
def ar(a,b,c):
    if a+b>c and a+c>b and b+c>a and a>0 and b>0 and c>0:
        s=(a+b+c)/2
        area= ((s*(s-a)*(s-b)*(s-c)))**(0.5)
        return area
print( ar(3,4,5))
