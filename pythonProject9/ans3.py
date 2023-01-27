n = int(input("Please enter the number of rows of Pascal's triangle: "))
for i in range(0, n):
    for j in range(n - i + 1):
        print(end=" ")
    from math import factorial

    for j in range(0, i + 1):
        print(factorial(i) // (factorial(j) * factorial(i - j)), end=" ")

    print()