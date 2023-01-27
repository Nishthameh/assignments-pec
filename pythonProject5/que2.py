year=int(input("enter a year"))
if(year%4==0) and (year%100!=0):
    leap=True
elif(year%100==0)and (year%400==0):
    leap= True
else:
    leap=False
d1={True:"yes,it is a leap year", False:"no, it is not a leap year"}
print(d1[leap])

