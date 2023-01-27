


import random

for count in range(1,11):

 randnum1=random.randint(1,10)
 randnum2=random.randint(1,10)
 y=randnum1*randnum2
 print(f"{randnum1}*{randnum2}=")
 x=int(input())
 if x==y:
     print(f"right, answer is {y}")


 else:
     print(f"wrong, answer is {y}")



