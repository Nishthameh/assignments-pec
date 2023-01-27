my_str=str(input('Please enter the string: '))
def pangram(my_str):
    alphabets='abcdefghijklmnopqrstuvwxyz'
    for char in alphabets:
        if char not in my_str.lower():
            return False
    return True

if (pangram(my_str)) is True:
    print(my_str,'is a Pangram.')
else:
    print(my_str,'is not a Pangram.')