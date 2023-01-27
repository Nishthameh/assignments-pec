marks=int(input("enter your marks"))
if marks>80:
    grade="A"
elif 80>marks>60:
    grade="B"
elif 60>marks>50:
    grade="C"
elif 50>marks>45:
    grade="D"
elif 45>marks>25:
    grade="E"
else:
    grade="F"
    print(f"your grade is {grade}")